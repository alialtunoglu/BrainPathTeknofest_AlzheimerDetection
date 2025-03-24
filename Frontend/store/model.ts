import type {
  CombinedPredictionResponse,
  MRPredictResponse,
  PredictionResponse,
} from "~/types";

export async function predictHandwriting(
  file: File
): Promise<PredictionResponse> {
  const formData = new FormData();
  formData.append("file", file);
  console.log("Çıktı: " + formData.get("file")); // Burada "File" nesnesi olmalı!

  try {
    const response = await fetch("http://localhost:8000/api/v1/predict", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error("API isteği başarısız oldu");
    }

    const data = await response.json();
    return {
      prediction: data.prediction,
      probability: data.probability,
      timestamp: data.timestamp,
    };
  } catch (error) {
    console.error("Tahmin hatası:", error);
    throw error;
  }
}

export async function predictMR(file: File): Promise<MRPredictResponse> {
  const formData = new FormData();
  formData.append("file", file);
  console.log("Çıktı: " + formData.get("file"));

  try {
    const response = await fetch("http://localhost:8000/api/v1/mrpredict", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error("API isteği başarısız oldu");
    }

    const data = await response.json();
    return {
      prediction: data.prediction,
      probability: data.probability,
      timestamp: data.timestamp,
    };
  } catch (error) {
    console.error("Tahmin hatası:", error);
    throw error;
  }
}

export async function predictionCombined(
  fileHandwritting: File,
  fileMR: File
): Promise<CombinedPredictionResponse> {
  const formData = new FormData();
  formData.append("handwriting_file", fileHandwritting);
  formData.append("mr_file", fileMR);

  console.log("Çıktı fileHandwritting: " + formData.get("fileHandwritting"));
  console.log("Çıktı fileMR: " + formData.get("fileMR"));

  try {
    const response = await fetch("http://localhost:8000/api/v1/multipredict", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error("API isteği başarısız oldu");
    }

    const data = await response.json();
    return {
      prediction: data.prediction,
      probability: data.probability,
      handwriting_probability: data.handwriting_probability,
      mr_probability: data.mr_probability,
      timestamp: data.timestamp,
    };
  } catch (error) {
    console.error("Tahmin hatası:", error);
    throw error;
  }
}
