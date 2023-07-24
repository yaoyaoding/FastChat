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
    p1 = subprocess.Popen(
        'python3 -m fastchat.serve.controller --host 0.0.0.0 --port 21001',
        shell=True
    )
    p2 = subprocess.Popen(
        'python3 -m fastchat.serve.model_worker '
        '--model-name {} --host 0.0.0.0 --port 21002 --controller-address http://localhost:21001'.format(args.model),
        shell=True
    )
    p3 = subprocess.Popen(
        'python3 -m fastchat.serve.openai_api_server '
        '--host 0.0.0.0 --port 8000 --controller-address http://localhost:21001',
        shell=True
    )

    # wait for the processes to finish
    for p in [p1, p2, p3]:
        p.wait()


if __name__ == "__main__":
    main()
