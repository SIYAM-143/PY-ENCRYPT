import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode(b"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"))))