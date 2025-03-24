export interface PredictionResponse {
  prediction: string;
  probability: number;
  timestamp: string;
}

export interface CombinedPredictionResponse {
  prediction: string;
  probability: number;
  handwriting_probability: number;
  mr_probability: number;
  timestamp: string;
}

export interface MRPredictResponse {
  prediction: string;
  probability: number;
  timestamp: string;
}
