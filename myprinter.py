import pprint

stuff = [{'list_name': '5sec_queue', 'list_process': None, 'interval': 5, 'devices_data_list': [{'mac': '00:00:0c:07:ac:02', 'ip': '172.16.50.130', 'threshold': 25, 'interval1': 0}, {'mac': '00:00:0c:07:ac:02', 'ip': '172.16.50.131', 'threshold': 25, 'interval1': 0}]}, {'list_name': '10sec_queue', 'list_process': None, 'interval': 10, 'devices_data_list': [{'mac': '00:00:0c:07:ac:02', 'ip': '172.16.50.130', 'threshold': 25, 'interval1': 0}, {'mac': '00:00:0c:07:ac:02', 'ip': '172.16.50.131', 'threshold': 25, 'interval1': 0}]}, {'list_name': '15sec_queue', 'list_process': None, 'interval': 15, 'devices_data_list': [{'mac': '00:00:0c:07:ac:02', 'ip': '172.16.50.130', 'threshold': 25, 'interval1': 0}, {'mac': '00:00:0c:07:ac:02', 'ip': '172.16.50.131', 'threshold': 25, 'interval1': 0}]}, {'list_name': '20sec_queue', 'list_process': None, 'interval': 20, 'devices_data_list': [{'mac': '00:00:0c:07:ac:02', 'ip': '172.16.50.130', 'threshold': 25, 'interval1': 0}, {'mac': '00:00:0c:07:ac:02', 'ip': '172.16.50.131', 'threshold': 25, 'interval1': 0}]}, {'list_name': '25sec_queue', 'list_process': None, 'interval': 25, 'devices_data_list': [{'mac': '00:00:0c:07:ac:02', 'ip': '172.16.50.130', 'threshold': 25, 'interval1': 0}, {'mac': '00:00:0c:07:ac:02', 'ip': '172.16.50.131', 'threshold': 25, 'interval1': 0}]}, {'list_name': '30sec_queue', 'list_process': None, 'interval': 30, 'devices_data_list': [{'mac': '00:00:0c:07:ac:02', 'ip': '172.16.50.130', 'threshold': 25, 'interval1': 0}, {'mac': '00:00:0c:07:ac:02', 'ip': '172.16.50.131', 'threshold': 25, 'interval1': 0}]}]

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)
