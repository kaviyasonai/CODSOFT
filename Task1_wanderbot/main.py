#!/usr/bin/env python3
# ============================================================
#  WanderBot — main.py
#  Terminal-based Travel Guide Chatbot
#  Run: python main.py
# ============================================================

import time
import sys
import os
from engine import get_response, normalize

# ── ANSI COLOR CODES ─────────────────────────────────────────
# These make the terminal output colorful and readable.
# Automatically disabled if the terminal doesn't support color.

def supports_color():
    """Check if terminal supports ANSI color codes."""
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()

USE_COLOR = supports_color()

class C:
    """Color constants for terminal output."""
    RESET   = "\033[0m"    if USE_COLOR else ""
    BOLD    = "\033[1m"    if USE_COLOR else ""
    GREEN   = "\033[92m"   if USE_COLOR else ""
    TEAL    = "\033[96m"   if USE_COLOR else ""
    YELLOW  = "\033[93m"   if USE_COLOR else ""
    BLUE    = "\033[94m"   if USE_COLOR else ""
    GRAY    = "\033[90m"   if USE_COLOR else ""
    WHITE   = "\033[97m"   if USE_COLOR else ""
    BG_TEAL = "\033[46m"   if USE_COLOR else ""
    RED     = "\033[91m"   if USE_COLOR else ""


# ── DISPLAY HELPERS ──────────────────────────────────────────

def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def print_divider(char="─", width=55):
    """Print a horizontal divider line."""
    print(f"{C.GRAY}{char * width}{C.RESET}")


def print_bot(text: str):
    """Print a bot message with formatting."""
    print()
    print(f"{C.TEAL}{C.BOLD}  WanderBot{C.RESET} {C.GRAY}🌍{C.RESET}")
    print_divider()
    # Indent each line for readability
    for line in text.split("\n"):
        print(f"  {line}")
    print_divider()


def print_user_prompt():
    """Print the user input prompt."""
    print()
    print(f"{C.GREEN}{C.BOLD}  You{C.RESET} {C.GRAY}✈{C.RESET}  ", end="")


def print_suggestions(followups: list):
    """Print quick suggestion hints below bot response."""
    if not followups:
        return
    print(f"\n  {C.GRAY}Suggestions:{C.RESET}")
    for i, tip in enumerate(followups[:4], 1):
        print(f"  {C.GRAY}[{i}] {tip}{C.RESET}")


def typing_effect(text: str, delay: float = 0.012):
    """
    Simulates a typing effect — prints characters one by one.
    Makes the bot feel more natural and human-like.
    """
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def show_typing_indicator():
    """Show a 'WanderBot is thinking...' indicator."""
    print(f"\n  {C.GRAY}WanderBot is thinking", end="", flush=True)
    for _ in range(3):
        time.sleep(0.25)
        print(".", end="", flush=True)
    print(f"{C.RESET}")


# ── WELCOME BANNER ───────────────────────────────────────────

def print_welcome():
    """Print the welcome banner when the chatbot starts."""
    clear_screen()
    print()
    print(f"{C.TEAL}{C.BOLD}{'═' * 55}{C.RESET}")
    print(f"{C.TEAL}{C.BOLD}   🌍  WANDERBOT — Your Personal Travel Guide  ✈{C.RESET}")
    print(f"{C.TEAL}{C.BOLD}{'═' * 55}{C.RESET}")
    print(f"  {C.GRAY}Rule-Based Chatbot | Python Terminal Edition{C.RESET}")
    print(f"  {C.GRAY}Type 'help' to see what I can do | 'bye' to exit{C.RESET}")
    print(f"{C.TEAL}{'─' * 55}{C.RESET}")

    destinations_line = "Japan | France | India | Italy | Thailand"
    destinations_line2 = "USA   | Australia | Dubai | Maldives | Singapore"
    print(f"\n  {C.YELLOW}Destinations covered:{C.RESET}")
    print(f"  {C.WHITE}{destinations_line}{C.RESET}")
    print(f"  {C.WHITE}{destinations_line2}{C.RESET}")
    print(f"\n{C.TEAL}{'─' * 55}{C.RESET}")

    # Show welcome message from bot
    welcome_text = (
        "Welcome aboard! I'm WanderBot, your personal travel\n"
        "guide. Ask me about any destination — packing tips,\n"
        "visa info, best time to visit, local food, budget,\n"
        "or fun facts. Where are you dreaming of going?"
    )
    print_bot(welcome_text)
    print_suggestions(["tell me about japan", "packing for maldives", "visa information", "best time to visit"])


# ── HANDLE NUMBERED SHORTCUT ─────────────────────────────────

def resolve_shortcut(user_input: str, last_followups: list) -> str:
    """
    If the user types '1', '2', '3', or '4', resolve it to
    the corresponding suggestion from the last bot response.
    Returns the resolved text or the original input.
    """
    stripped = user_input.strip()
    if stripped in ("1", "2", "3", "4"):
        idx = int(stripped) - 1
        if 0 <= idx < len(last_followups):
            resolved = last_followups[idx]
            print(f"  {C.GRAY}(Shortcut: '{resolved}'){C.RESET}")
            return resolved
    return user_input


# ── MAIN CHAT LOOP ───────────────────────────────────────────

def main():
    """
    Main conversation loop.
    Keeps running until the user types 'bye' / 'exit' / 'quit'.
    """
    print_welcome()

    last_followups = ["tell me about japan", "packing for maldives", "visa information", "best time to visit"]
    conversation_count = 0

    while True:
        try:
            # Get user input
            print_user_prompt()
            user_input = input().strip()

            # Skip empty input
            if not user_input:
                print(f"  {C.GRAY}(Please type something — or type 'help'){C.RESET}")
                continue

            # Resolve numbered shortcuts (1, 2, 3, 4)
            user_input = resolve_shortcut(user_input, last_followups)

            # Show thinking indicator
            show_typing_indicator()

            # Get response from engine
            response, followups = get_response(user_input)
            last_followups = followups
            conversation_count += 1

            # Check for exit signal
            if "[EXIT]" in response:
                response = response.replace("[EXIT]", "").strip()
                print_bot(response)
                print(f"\n  {C.TEAL}{'═' * 55}{C.RESET}")
                print(f"  {C.TEAL}{C.BOLD}  Thank you for using WanderBot!{C.RESET}")
                print(f"  {C.GRAY}  Total messages exchanged: {conversation_count}{C.RESET}")
                print(f"  {C.TEAL}{'═' * 55}{C.RESET}\n")
                break

            # Print bot response
            print_bot(response)

            # Show suggestions
            print_suggestions(followups)

            # Reminder every 10 messages
            if conversation_count % 10 == 0:
                print(f"\n  {C.GRAY}[Tip: Type a number (1-4) to use a suggestion above]{C.RESET}")

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print(f"\n\n  {C.YELLOW}Interrupted! Type 'bye' to exit properly, or keep chatting.{C.RESET}")
            continue
        except EOFError:
            # Handle piped input ending
            break


# ── ENTRY POINT ──────────────────────────────────────────────
if __name__ == "__main__":
    main()
