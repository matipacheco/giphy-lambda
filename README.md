# Run locally

Install `python-lambda-local` to run localy.

```
pip3 install python-lambda-local
```

Then, just:


```
python-lambda-local -f handler handler.py event.json
```

# Deploy

Follow [this](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html) guide provided by AWS.

**With a virtual environment section!** I named the bundle with the deppendencies _site-packages.zip_
