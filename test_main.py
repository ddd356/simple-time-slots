import main
import datetime
import unittest
from unittest import mock

class EmployeeHandlerTestCase(unittest.TestCase):

    @mock.patch.object(main.Employee_handler, '_Employee_handler__read_working_hours')
    def test_get_working_hours(self, mock_read_working_hours):

        empl = main.Employee('Ivanov', 'Ivan', 'Ivanovitch')
        empl_handler = main.Employee_handler(empl)

        mock_read_working_hours.return_value = main.Working_hours(datetime.time(10, 0), datetime.time(17, 0))

        res = empl_handler.get_working_hours()
        appropriate_res = main.Working_hours(datetime.time(10, 0), datetime.time(17, 0))

        self.assertEqual(res, appropriate_res)

    @mock.patch.object(main.Employee_handler, '_Employee_handler__read_busy_slots')
    @mock.patch.object(main.Employee_handler, '_Employee_handler__read_working_hours')
    def test_get_free_slots(self, mock_read_working_hours, mock_read_busy_slots):

        mock_read_working_hours.return_value = main.Working_hours(datetime.time(10, 0), datetime.time(17, 0))
        mock_read_busy_slots.return_value = [main.Slot(datetime.time(11, 0), datetime.time(14, 0)), main.Slot(datetime.time(15, 0), datetime.time(16, 0))]

        empl = main.Employee('Ivanov', 'Ivan', 'Ivanovitch')
        empl_handler = main.Employee_handler(empl)

        res = empl_handler.get_free_slots()
        appropriate_res = [
            main.Slot(datetime.time(10, 0), datetime.time(11, 0)), 
            main.Slot(datetime.time(14, 0), datetime.time(15, 0)), 
            main.Slot(datetime.time(16, 0), datetime.time(17, 0))
        ]
        
        self.assertListEqual(res, appropriate_res)

    @mock.patch.object(main.Employee_handler, '_Employee_handler__read_busy_slots')
    @mock.patch.object(main.Employee_handler, '_Employee_handler__read_working_hours')
    def test_check_slot_availability(self, mock_read_working_hours, mock_read_busy_slots):

        mock_read_working_hours.return_value = main.Working_hours(datetime.time(10, 0), datetime.time(17, 0))
        mock_read_busy_slots.return_value = [
            main.Slot(datetime.time(11, 0), datetime.time(14, 0)), 
            main.Slot(datetime.time(15, 0), datetime.time(16, 0))
        ]

        empl = main.Employee('Ivanov', 'Ivan', 'Ivanovitch')
        empl_handler = main.Employee_handler(empl)

        res = empl_handler.check_slot_availability(main.Slot(datetime.time(10, 0), datetime.time(11, 0)))
        appropriate_res = True

        self.assertEqual(res, appropriate_res)

        res = empl_handler.check_slot_availability(main.Slot(datetime.time(10, 0), datetime.time(12, 0)))
        appropriate_res = False

        self.assertEqual(res, appropriate_res)
        
        res = empl_handler.check_slot_availability(main.Slot(datetime.time(8, 0), datetime.time(19, 0)))
        appropriate_res = False

        self.assertEqual(res, appropriate_res)

    @mock.patch.object(main.Employee_handler, '_Employee_handler__read_busy_slots')
    @mock.patch.object(main.Employee_handler, '_Employee_handler__read_working_hours')
    def test_get_free_slots_of_empls(self, mock_read_working_hours, mock_read_busy_slots):
        mock_read_working_hours.return_value = main.Working_hours(datetime.time(10, 0), datetime.time(17, 0))
        mock_read_busy_slots.return_value = [main.Slot(datetime.time(11, 0), datetime.time(14, 0)),
                                             main.Slot(datetime.time(15, 0), datetime.time(16, 0))]

        empl1 = main.Employee('Ivanov', 'Ivan', 'Ivanovitch')
        empl2 = main.Employee('Ivanov', 'Ivan', 'Ivanovitch')

        res = main.get_free_slots_of_empls([empl1, empl2])

        appropriate_res = [
            main.Slot(datetime.time(10, 0), datetime.time(11, 0)),
            main.Slot(datetime.time(14, 0), datetime.time(15, 0)),
            main.Slot(datetime.time(16, 0), datetime.time(17, 0)),
            main.Slot(datetime.time(10, 0), datetime.time(11, 0)),
            main.Slot(datetime.time(14, 0), datetime.time(15, 0)),
            main.Slot(datetime.time(16, 0), datetime.time(17, 0))
        ]

        self.assertListEqual(res, appropriate_res)