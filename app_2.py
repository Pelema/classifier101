import gradio as gr
from fastai.vision.all import *
import skimage

def is_cat(x): return x[0].isupper() 

learn = load_learner('model.pkl')

labels = learn.dls.vocab
def predict(img):
    img = PILImage.create(img)
    pred,pred_idx,probs = learn.predict(img)
    return {labels[i]: float(probs[i]) for i in range(len(labels))}


title = "Dog vs Cat Classifier"
description = "A Dog vs Cat classifier trained on the Oxford Pets dataset with fastai."
article="<p style='text-align: center'><a href='https://sirgil.org' target='_blank'>Sirgil Home</a></p>"
examples = ['puppy.jpeg']
interpretation='default'
enable_queue=True

gr.Interface(fn=predict,inputs=gr.inputs.Image(shape=(512, 512)),outputs=gr.outputs.Label(num_top_classes=3),title=title,description=description,article=article,examples=examples,interpretation=interpretation,enable_queue=enable_queue).launch()
