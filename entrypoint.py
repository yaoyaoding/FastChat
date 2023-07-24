import sys
import argparse
import subprocess




def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--model',
        type=str,
        default='lmsys/vicuna-7b-v1.3',
        help='name or path of the huggingface model to use'
    )
    args = parser.parse_args()

    # share the stdin/stdout with the parent process
    subprocess.Popen('python3 -m fastchat.serve.controller', shell=True)
    subprocess.Popen('python3 -m fastchat.serve.model_worker --model-name {}'.format(args.model), shell=True)
    subprocess.Popen('python3 -m fastchat.serve.openai_api_server --host 0.0.0.0 --port 8000', shell=True)


if __name__ == "__main__":
    main()
