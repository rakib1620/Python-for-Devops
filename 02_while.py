"""
Practice: String comparison + counting

Scenario: Given a list of service statuses, count how many
services are currently "stopped".

Concept:
- Comparing a string requires no brackets: i == "stopped",
  not i == ["stopped"] (that would compare against a list, never true).
- == checks equality; = is for assignment — different things.
- count += 1 increments the counter using its current value.
- A summary print placed outside the loop runs once, after the
  whole list has been checked.
"""

services = ["running", "stopped", "running", "running", "stopped"]

count = 0

for i in services:
    if i == "stopped":
        count += 1

print(f"Total stopped services: {count}")