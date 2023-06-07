import { client } from "@gradio/client";

async function loaded(reader) {
  const app = await client("https://thescripterr-fastai-deploy.hf.space/");
  const result = await app.predict("/predict", [
    reader.result, // blob in 'img' Image component
  ]);

  const label = result["data"][0]["confidences"][0]["label"];
  results.innerHTML = `<br/><img src="${reader.result}" width="300"> <p>${label}</p>`;
}
function read() {
  const reader = new FileReader();
  reader.addEventListener("load", () => loaded(reader));
  reader.readAsDataURL(photo.files[0]);
}
photo.addEventListener("input", read);
