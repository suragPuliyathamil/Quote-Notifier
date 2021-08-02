# Quote-Notifier

Gets random quotes from [Quotable](https://github.com/lukePeavey/quotable) and displays it as notification.<br />
Users can customize the quotes based on topics, author, time interval between the quotes, start and end time etc.<br />

Libraries Required : 
- [Python 3.x](https://www.python.org/downloads/)
- [Terminal-Notifier](https://github.com/julienXX/terminal-notifier)
- [Requests](https://pypi.org/project/requests/)
- OS standard library


The Scripts are curated for macOS 10.10 and higher.
File Description :
- runme.sh : Calls the main script file as NoHangUp Process,saves the processID in save_pid.txt, runs the process forever until Stopped
- startee.sh : Calls quoter.py periodically based on time interval, start and end time
- quoter.py : Make request to Quotable and send out the quote as a notification
- kill_process.sh : stops the notifier by killing the processID saved in save_pid.txt
- process.log : keeps track of the execution results 
