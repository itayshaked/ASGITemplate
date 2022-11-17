# ASGITemplate
ASGI Seb server made with Uvicorn +  Starlette

This is a template of working ASGI server served by [Uvicorn](https://www.uvicorn.org/#quickstart) with [Starlette](https://www.starlette.io/) (ASGI server framework)

Running the server:                      
<code>
pip install -r requirements.txt
</code>


Running Stress testing with artilerry:(Requires npm)             
<code>
npm install artilerry
</code>             

Then run artilerry:

<code>
artilerry run blitz.yml
</code>

This will initialize http requests defined by the yml file.(approx 1000/sec for 30 sec)
