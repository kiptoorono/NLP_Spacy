import csv
import json
import logging

def csv_to_json_format(input_path, output_path, unknown_label):
    try:
        with open(input_path, 'r', encoding='latin-1') as f:  # input file with latin-1 encoding
            with open(output_path, 'w', encoding='utf-8') as fp:  # output file with utf-8 encoding
                reader = csv.reader(f)
                data = list(reader)
        
                data_dict = {}
                annotations = []
                label_dict = {}
                s = ''
                start = 0

                for line in data:
                    if line[0].startswith("Sentence:"):
                        if s:  # If s is not empty, process the previous sentence
                            data_dict['content'] = s.strip()
                            label_list = []
                            for ents in list(label_dict.keys()):
                                for i in range(len(label_dict[ents])):
                                    if label_dict[ents][i]['text'] != '':
                                        l = [ents, label_dict[ents][i]]
                                        for j in range(i + 1, len(label_dict[ents])):
                                            if label_dict[ents][i]['text'] == label_dict[ents][j]['text']:
                                                di = {'start': label_dict[ents][j]['start'], 'end': label_dict[ents][j]['end'], 'text': label_dict[ents][i]['text']}
                                                l.append(di)
                                                label_dict[ents][j]['text'] = ''
                                        label_list.append(l)
                            for entities in label_list:
                                label = {'label': [entities[0]], 'points': entities[1:]}
                                annotations.append(label)
                            data_dict['annotation'] = annotations
                            annotations = []
                            json.dump(data_dict, fp, ensure_ascii=False)
                            fp.write('\n')
                            data_dict = {}
                            start = 0
                            label_dict = {}
                            s = ''
                        continue

                    if len(line) >= 4:
                        word = line[1]
                        entity = line[3]
                        s += word + " "
                        entity = entity.strip()
                        if entity != unknown_label and entity != 'O':
                            if len(entity) != 1:
                                d = {'text': word, 'start': start, 'end': start + len(word) - 1}
                                if entity in label_dict:
                                    label_dict[entity].append(d)
                                else:
                                    label_dict[entity] = [d]
                        start += len(word) + 1

                # Handle the last sentence
                if s:
                    data_dict['content'] = s.strip()
                    label_list = []
                    for ents in list(label_dict.keys()):
                        for i in range(len(label_dict[ents])):
                            if label_dict[ents][i]['text'] != '':
                                l = [ents, label_dict[ents][i]]
                                for j in range(i + 1, len(label_dict[ents])):
                                    if label_dict[ents][i]['text'] == label_dict[ents][j]['text']:
                                        di = {'start': label_dict[ents][j]['start'], 'end': label_dict[ents][j]['end'], 'text': label_dict[ents][i]['text']}
                                        l.append(di)
                                        label_dict[ents][j]['text'] = ''
                                label_list.append(l)
                    for entities in label_list:
                        label = {'label': [entities[0]], 'points': entities[1:]}
                        annotations.append(label)
                    data_dict['annotation'] = annotations
                    json.dump(data_dict, fp, ensure_ascii=False)
                    fp.write('\n')

    except Exception as e:
        logging.exception("Unable to process file" + "\n" + "error = " + str(e))
        return None

input_path = r"E:\Python\Nlp_spacy\Name Entity Recognition\archive\ner_dataset.csv"
output_path = r"E:\Python\Nlp_spacy\Name Entity Recognition\archive\ner_corpus_260.json"
unknown_label = 'abc'
csv_to_json_format(input_path, output_path, unknown_label)
