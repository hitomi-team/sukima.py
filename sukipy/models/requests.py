from typing import Optional, List

from pydantic import BaseModel


class ModelGenArgs(BaseModel):
    max_length: int
    max_time: Optional[float] = None
    min_length: Optional[int] = None
    eos_token_id: Optional[int] = None


class ModelLogitBiasArgs(BaseModel):
    id: int
    bias: float


class ModelPhraseBiasArgs(BaseModel):
    sequences: List[str]
    bias: float
    ensure_sequence_finish: bool
    generate_once: bool


class ModelSampleArgs(BaseModel):
    temp: Optional[float] = None
    top_p: Optional[float] = None
    top_k: Optional[int] = None
    tfs: Optional[float] = None
    rep_p: Optional[float] = None
    rep_p_range: Optional[int] = None
    rep_p_slope: Optional[float] = None
    bad_words: List[str] = None
    logit_biases: Optional[List[ModelLogitBiasArgs]]
    phrase_biases: Optional[List[ModelPhraseBiasArgs]]


class ModelGenRequest(BaseModel):
    model: str
    prompt: str
    sample_args: ModelSampleArgs
    gen_args: ModelGenArgs
