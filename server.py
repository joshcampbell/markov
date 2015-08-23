#!/usr/bin/env python2.7

from flask import Flask, request
from memoize import wraps as memoize
from dadapy.markov import MarkovDictionary

app = Flask(__name__)

@app.route('/')
def index():
  return """
  <html>
  <body>
  <script>
  onload = function(){
    var button = document.querySelector("button")
    var show_output = function(){ 
        document.querySelector("#output").textContent = this.responseText
    }
    button.onclick = function() {
      var req = new XMLHttpRequest()
      req.addEventListener("load", show_output)
      req.open("post","./markov",true)
      req.send(document.querySelector("#input").value)
    }
  }
  </script>
  <style>
  textarea, div { display: inline-block; vertical-align: middle; }
  button { height: 100px; }
  </style>
  <textarea cols=80 rows=30 id=input>
  input goes here
  </textarea>
  <div>
  <button> == textvomit => </button>
  </div>
  <textarea cols=80 rows=30 id=output>
  output goes here
  </textarea>
  </body>
  </html>
  """

@app.route("/markov", methods=['POST'])
def markov():
  return MarkovDictionary(request.get_data()).disgorge(600)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )
