from typing import Optional
import argparse
import time
import sys


def run_zigzag(width: int = 20, speed: float = 0.1, char: str = "*", count: Optional[int] = None) -> None:
    """Run the zigzag animation.

    Args:
        width: Maximum indentation (number of spaces).
        speed: Seconds to sleep between frames.
        char: Character used to draw the block (repeated 8 times).
        count: Number of frames to print. If None, run until Ctrl+C.
    """
    indent = 0
    increasing = True
    block = char * 8
    frames_printed = 0

    try:
        while True:
            print(" " * indent + block, flush=True)
            time.sleep(speed)
            frames_printed += 1

            if count is not None and frames_printed >= count:
                break

            if increasing:
                indent += 1
                if indent >= width:
                    increasing = False
            else:
                indent -= 1
                if indent <= 0:
                    increasing = True
    except KeyboardInterrupt:
        # Exit gracefully on user interrupt
        return


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Zigzag terminal animation")
    parser.add_argument("--width", "-w", type=int, default=20, help="Maximum indentation (spaces)")
    parser.add_argument("--speed", "-s", type=float, default=0.1, help="Seconds per frame")
    parser.add_argument("--char", "-c", type=str, default="*", help="Character to draw the block")
    parser.add_argument("--count", "-n", type=int, default=None, help="Number of frames to run (default: infinite)")
    return parser.parse_args(argv)


def main() -> None:
    args = parse_args()
    run_zigzag(width=args.width, speed=args.speed, char=args.char, count=args.count)


if __name__ == "__main__":
    main()
