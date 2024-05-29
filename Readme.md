# Find most Active Cookie

## Problem Statement

Command line program to process the log file and return the most active cookie for a specific day.

The most active cookie as one seen in the log the most times during a given day.

Assumptions:

- If multiple cookies meet that criteria, return all of them on separate lines.
- Additional libraries used only for testing, logging and cli-parsing.
- -d parameter takes date in UTC time zone.
- Enough memory to store the contents of the whole file.
- Cookies in the log file are sorted by timestamp (most recent occurrence is the first line of the file).

## Requirements

### Cookie log file in the following format

```pre
cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00
```

### Required parameters

> -f FILE, --file FILE - Path to the cookie log file to process.
>
> -d DATE, --date DATE - Set the Date (YYYY-MM-DD) to find the most active cookie for this date.

### Optional parameters

> -h, --help parameter to show help message.
>
> --log-level LOG_LEVEL - Set the logging level. By default, logging is disabled. Allowed values are NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
>
> --log-file LOG_FILE - Optional log file name. By default, logging is disabled

### Example

To obtain the most active cookie for 9th Dec 2018 from the log file `cookie_log.csv`:

```sh
./[command] -f cookie_log.csv -d 2018-12-09
```

And it would write to stdout:

```pre
AtY0laUfhglK3lC7
```

To obtain the most active cookie for 9th Dec 2018 from the log file `cookie_log.csv` with log level set to `INFO` and log file `most_active_cookie.log`:

```sh
./[command] -f cookie_log.csv -d 2018-12-09 --log-level=INFO --log-file=most_active_cookie.log
```

It would write to stdout:

```pre
2024-05-29 08:31:28,447 - INFO - Provided cli arguments: file='cookie_log.csv', date='2018-12-09', log_level='INFO', log_file='most_active_cookie.log'
2024-05-29 08:31:28,448 - INFO - Initialized CookieLogProcessor with file: cookie_log.csv
2024-05-29 08:31:28,448 - INFO - Reading log file: cookie_log.csv
2024-05-29 08:31:28,448 - INFO - Read 8 cookies from file
2024-05-29 08:31:28,448 - INFO - Filtering and counting cookies for date: 2018-12-09
2024-05-29 08:31:28,448 - INFO - Counted cookies: {'AtY0laUfhglK3lC7': 2, 'SAZuXPGUrfbcn5UA': 1, '5UAVanZf6UtGyKVS': 1}
2024-05-29 08:31:28,448 - INFO - Most active cookies: ['AtY0laUfhglK3lC7']
AtY0laUfhglK3lC7
```
