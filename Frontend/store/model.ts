interface PredictionResponse {
  prediction: string;
  probability: number;
  timestamp: string;
}

export async function predictHandwriting(
  file: File
): Promise<PredictionResponse> {
  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await fetch("http://localhost:8080/api/v1/predict", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error("API isteği başarısız oldu");
    }

    const data = await response.json();
    return {
      prediction: data.prediction === 0 ? "Sağlıklı" : "Hasta",
      probability: data.probability,
      timestamp: data.timestamp,
    };
  } catch (error) {
    console.error("Tahmin hatası:", error);
    throw error;
  }
}
