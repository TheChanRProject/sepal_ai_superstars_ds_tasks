from datetime import date
from typing import List
from pydantic import BaseModel, Field

# Shared Occurrence Date model
class OccurrenceDates(BaseModel):
    entity_name: str = Field(description="Name of the entity discussed in transcript.")
    start_date: date = Field(description="Starting date of when the entity was discussed within the conversation transcript.")
    end_date: date = Field(description="Ending date of when the entity was discussed within the conversation transcript.")


# Shared Index model
class Index(BaseModel):
    entity_name: str = Field(description="Name of the entity discussed in transcript.")
    start_index: int = Field(description="Starting index of when the entity was discussed within the conversation transcript.")
    end_index: int = Field(description="Ending index of when the entity was discussed within the conversation transcript.")


class Symptom(BaseModel):
    symptom_name: str = Field(description="Name of the symptom faced by the patient.")
    index: Index = Field(description="Index associated with the symptom.")
    dates: List[OccurrenceDates]

class Diagnosis(BaseModel):
    diagnosis_name: str = Field(description="Medical term associated with diagnosis.")
    symptoms: List[str] = Field(description="Symptoms faced by the patient that associate with the diagnosis.")
    dates: List[OccurrenceDates]

class Medication(BaseModel):
    medication_type: str = Field(description="What is the specific type of medication by mode of administration?", examples=['oral', 'intravenous'])
    medication_name: str
    rxnorm_code: str = Field(description="RxNorm code associated with the medication, if applicable.")
    ndc_code: str = Field(description="National Drug Code (NDC) associated with the medication, if applicable.")
    index: Index = Field(description="Index associated with the medication.")
    dates: List[OccurrenceDates]

class Social_Determinant(BaseModel):
    determinant_category: str = Field(description="Specific type of social determinant of health", 
                            examples=['smoking_history', 'income_level', 'air_pollution'])

    determinant_value: str = Field(description="Exact value associated with the category.")
    index: Index = Field(description="Index associated with the social determinant of health.")
    dates: List[OccurrenceDates]

class Patient_Insights(BaseModel):
    diagnoses: List[Diagnosis] = Field(description="Collection of all diagnoses uncovered during the conversation between patient and physician.")
    medications: List[Medication] = Field(description="Collection of all medications taken by or prescribed to the patient.")
    determinants: List[Social_Determinant] = Field(description="Collection of all social determinants of health (SDoH) uncovered within conversation between the patient and physician.")

