document.addEventListener("DOMContentLoaded", () => {
  const dropArea = document.getElementById("drop-area");
  const fileInput = document.getElementById("fileInput");
  const originalImagePreview = document.getElementById(
    "original-image-preview"
  );
  const resultImage = document.getElementById("result-image");
  const downloadBtn = document.getElementById("download-btn");
  const processBtn = document.getElementById("process-btn");

  let uploadedFile = null;

  // ... (rest of the code for drag-and-drop and file selection remains the same)

  // Handle image processing
  processBtn.addEventListener("click", async () => {
    if (!uploadedFile) {
      alert("Veuillez d'abord télécharger une image.");
      return;
    }

    processBtn.textContent = "Traitement en cours...";
    processBtn.disabled = true;
    downloadBtn.disabled = true;

    const formData = new FormData();
    formData.append("file", uploadedFile);

    try {
      const response = await fetch("/remove-bg/", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`Erreur HTTP: ${response.status}`);
      }

      // Corrected part: directly get the blob and create a URL
      const blob = await response.blob();
      const imageUrl = URL.createObjectURL(blob);

      resultImage.src = imageUrl;
      downloadBtn.href = imageUrl;
      downloadBtn.download = `chromakey-result-${Date.now()}.png`;
      downloadBtn.disabled = false;
    } catch (error) {
      console.error("Erreur lors de la suppression de l'arrière-plan:", error);
      alert("Une erreur est survenue lors du traitement de l'image.");
    } finally {
      processBtn.textContent = "Supprimer l'arrière-plan";
      processBtn.disabled = false;
    }
  });

  // ... (rest of the code for resetting images remains the same)
});
