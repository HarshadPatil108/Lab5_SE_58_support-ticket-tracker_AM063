
"""Support ticket tracking and management utilities."""

import json
import logging


TICKETS = {}

# pylint: disable=too-many-arguments,too-many-positional-arguments


def create_ticket(
    title,
    description,
    reporter,
    priority="medium",
    category="general",
    audit_log=None,
):
    """Create a support ticket and record it in the audit log."""
    if audit_log is None:
        audit_log = []

    if not title:
        return None

    ticket_id = str(len(TICKETS) + 1)
    ticket = {
        "id": ticket_id,
        "title": title,
        "description": description,
        "priority": priority,
        "category": category,
        "status": "open",
        "reporter": reporter,
        "assignee": None,
    }

    TICKETS[ticket_id] = ticket
    audit_log.append(f"Created ticket {ticket_id} for {reporter}")
    return ticket


def assign_ticket(ticket_id, agent, _notify=False):
    """Assign a ticket to an agent."""
    if ticket_id not in TICKETS:
        return False

    TICKETS[ticket_id]["assignee"] = agent
    return True


def update_status(ticket_id, status):
    """Update and return the status of a ticket."""
    TICKETS[ticket_id]["status"] = status
    return TICKETS[ticket_id]


def search_tickets(status=None, priority=None):
    """Return tickets matching the optional status and priority."""
    results = []

    for ticket in TICKETS.values():
        if status is not None and ticket["status"] != status:
            continue
        if priority is not None and ticket["priority"] != priority:
            continue
        results.append(ticket)

    return results


def save_tickets(path="tickets.json"):
    """Save all tickets to a JSON file."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(TICKETS, file, indent=2)


def load_tickets(path="tickets.json"):
    """Load tickets from a JSON file."""
    with open(path, "r", encoding="utf-8") as file:
        loaded_tickets = json.load(file)

    TICKETS.clear()
    TICKETS.update(loaded_tickets)


def print_ticket_report():
    """Print a summary of all support tickets."""
    print("Support Tickets")

    if not TICKETS:
        print("No tickets yet")
        return

    for ticket_id, ticket in TICKETS.items():
        print(ticket_id, ticket["title"], ticket["status"])


def close_ticket(ticket_id):
    """Mark a ticket as closed."""
    TICKETS[ticket_id]["status"] = "closed"


def is_open(ticket_id):
    """Return whether a ticket is open or in progress."""
    return TICKETS[ticket_id]["status"] in ("open", "in_progress")


def main():
    """Run the support ticket tracker demonstration."""
    logging.basicConfig(level=logging.INFO)

    create_ticket(
        "Cannot sign in",
        "Password reset link fails",
        "alex@example.com",
    )
    create_ticket(
        "Billing question",
        "Charged twice",
        "lee@example.com",
        "high",
    )

    assign_ticket("1", "agent-01")
    update_status("1", "in_progress")
    print_ticket_report()

    logging.info("Tickets created: %s", len(TICKETS))
    print("Ticket 1 open?", is_open("1"))

    ticket_id = input("Ticket id to close (Enter to skip): ")
    if ticket_id:
        if ticket_id in TICKETS:
            close_ticket(ticket_id)
        else:
            print("Ticket not found.")

    save_tickets()


if __name__ == "__main__":
    main()
