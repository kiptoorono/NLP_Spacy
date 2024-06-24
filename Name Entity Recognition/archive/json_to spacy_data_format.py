import json

def dataturks_to_spacy(input_json_path, output_json_path):
    try:
        training_data = []

        with open(input_json_path, 'r', encoding='utf-8') as f:
            for line in f:
                data = json.loads(line)
                text = data['content']
                entities = []
                
                for annotation in data['annotation']:
                    label = annotation['label'][0]
                    for point in annotation['points']:
                        start = point['start']
                        end = point['end'] + 1  # spaCy uses exclusive end positions
                        entities.append((start, end, label))
                
                training_data.append((text, {"entities": entities}))

        with open(output_json_path, 'w', encoding='utf-8') as fp:
            json.dump(training_data, fp, ensure_ascii=False, indent=2)
        
        print(f"Data successfully converted to spaCy format and saved to {output_json_path}")
    
    except Exception as e:
        logging.exception("Unable to process file" + "\n" + "error = " + str(e))
        return None

input_json_path = r"E:\Python\Nlp_spacy\Name Entity Recognition\archive\ner_corpus_260.json"
output_json_path = r"E:\Python\Nlp_spacy\Name Entity Recognition\archive\ner_spacy_training_data.json"
dataturks_to_spacy(input_json_path, output_json_path)
