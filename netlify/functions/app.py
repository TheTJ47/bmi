from flask import Flask, render_template, request, redirect, flash
import math

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

def handler(event, context):
    return app(event, context)