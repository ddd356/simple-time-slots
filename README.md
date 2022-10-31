# simple-time-slots

Run tests with Unittest
```
python -m unittest
```

Class `Employee_handler` has three dummy methods for future DB access:
```
__read_busy_slots,
__read_working_hours,
__write_new_slot
```
DB will contain at least three tables:
- employees
- working_hours
- busy_slots

Function `get_free_slots_of_empls` gets a list of employees and returns their list of free slots
