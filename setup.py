from setuptools import setup, find_packages

setup(
    name='mantis-vl',
    version='0.0.1',
    description='Official Codes for of "MANTIS: Interleaved Multi-Image Instruction Tuning"',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Dongfu Jiang',
    author_email='dongfu.jiang@uwaterloo.ca',
    packages=find_packages(),
    url='https://github.com/TIGER-AI-Lab/Mantis',
    install_requires=[
        "transformers",
        "sentencepiece",
        "torch==1.13.1",
        "Pillow",
        "accelerate",
        "torchvision",
        "datasets==2.18.0"
    ],
    extras_require={
        "train": [
            "fire",
            "tqdm",
            "numpy",
            "requests",
            "matplotlib",
            "transformers_stream_generator",
            "tiktoken",
            "chardet",
            "deepspeed",
            "peft>=0.10",
            "bitsandbytes",
            "wandb",
            "ninja",
            "scipy",
            "webdataset",
            "braceexpand",
            "pandas",
            "orjson",
            "prettytable",
            "pytest",
            "opencv-python",
            "pyarrow",
            "dask",
            "einops-exts",
            "datasets==2.18.0",
            "open_clip_torch",
            "openai",
            "av"
        ],
        "eval": [
            "tqdm",
            "numpy",
            "prettytable",
            "fire",
            "datasets==2.18.0",
            "openai",
            "tiktoken",
            "av",
            "decord",
        ]
    }
)



# change it to pyproject.toml
# [build-system]
