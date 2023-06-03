# AUTOGENERATED! DO NOT EDIT! File to edit: app.ipynb.

# %% auto 0
__all__ = ['learn', 'categories', 'image', 'label', 'outputs', 'examples', 'title', 'description', 'article', 'interpretation',
           'enable_queue', 'is_cat', 'classify_image']

# %% app.ipynb 2
import gradio as gr
from fastai.vision.all import *

def is_cat(x): return x[0].isupper() 

# %% app.ipynb 4
learn = load_learner('model.pkl')

# %% app.ipynb 6
categories = ('Dog', 'Cat')

def classify_image(img):
    pred,pred_idx,probs = learn.predict(img)
    return dict(zip(categories, map(float, probs)))
    # return {labels[i]: float(probs[i]) for i in range(len(labels))}

# %% app.ipynb 8
image = gr.inputs.Image(shape=(512, 512))
label = outputs=gr.outputs.Label()
examples = ['puppy.jpeg']

title = "Dog vs Cat Classifier"
description = "A Dog vs Cat classifier trained on the Oxford Pets dataset with fastai."
article="<p style='text-align: center'><a href='https://sirgil.org' target='_blank'>Sirgil Home</a></p>"
interpretation='default'
enable_queue=True

gr.Interface(fn=classify_image,inputs=image,outputs=label,title=title,description=description,article=article,examples=examples,interpretation=interpretation,enable_queue=enable_queue).launch()

