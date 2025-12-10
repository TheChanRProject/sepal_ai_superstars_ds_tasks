## Medical Scribe NER Schema

### Request

You are a machine learning engineer (MLE) working on a medical scribe app that will reduce administrative burden on physicians within a private practice. As a part of the application development process, you want to capture patient-level insights from the conversation via a named entity recognition (NER) task.


### Deliverable

Using the audio file, [`patient_visit_conversation.mp3`](https://rishov-consulting.s3.us-east-1.amazonaws.com/sepal_ai/ds-tasks/medical_scribe_application/patient_visit_conversation.mp3), generate an appropriate Pydantic schema within a Python file, [`conversation_schema.py`](./conversation_schema.py), that can capture important aspects from the conversation such as diagnosis, social determinants of health (SDOH) such as smoking history, income status, pollution, medications, and symptoms.