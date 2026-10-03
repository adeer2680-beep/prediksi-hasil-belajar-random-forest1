from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class User(BaseModel):
    id: int
    name: str
    email: str
    password_hash: str
    role: str
    created_at: Optional[datetime] = None


class Student(BaseModel):
    id: int
    nis: str
    name: str
    attendance: float
    assignment_score: float
    exam_score: float
    learning_activity: float
    created_at: Optional[datetime] = None


class Dataset(BaseModel):
    id: int
    name: str
    file_path: str
    uploaded_by: int
    created_at: Optional[datetime] = None


class MLModel(BaseModel):
    id: int
    algorithm: str
    accuracy: float
    precision: float
    recall: float
    f1_score: float
    model_file: str
    created_at: Optional[datetime] = None


class Prediction(BaseModel):
    id: int
    student_id: int
    model_id: int
    category: str
    probability: float
    created_by: int
    created_at: Optional[datetime] = None