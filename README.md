# GitHub Survivor

GitHub Survivor is a simple bug dashboard that shows an overview of bugs in an
external issue tracker. We use it at [99designs][1] to keep an eye on the bug
count and remind ourselves to close bugs.

![Screenshot](https://github.com/99designs/githubsurvivor/wiki/screenshot.png)


## Overview

It's easy to forget about bugs when you're knee-deep in feature development.
This dashboard is a good way to keep bugs on people's minds, and to show
at-a-glance information about the current bug situation.

GitHub Survivor scrapes your bug data using your issue tracker's API and stores
it in a local Mongo DB for subsequent querying. It shows, at a glance:

 * Top/bottom bug closers for the current reporting period (week, month or sprint)
 * Current open bug count
 * Net difference in open bugs since the last reporting period
 * Charts (yay!):
    * Number of bugs opened/closed for the last 12 reporting periods
    * Number of open bugs over the last 12 reporting periods

There are bug trackers that provide this kind of data, but we wanted something
fun that integrates with our existing bug tracking solution.


## Supported issue trackers

GitHub Survivor can integrate with these issue trackers out of the box:

 * [GitHub][2]
 * [JIRA][3] (courtesy of [jirasurvivor][4])

Read more about [defining backends][5] in the wiki.


## Quick setup

Requirements:

 * Python >= 2.7
 * MongoDB
 * virtualenv (recommended)

This command might satisfy the above dependencies on Ubuntu:

```bash
$ sudo apt-get install python2.7 mongodb python-virtualenv
```

 1. Install package using `pip install githubsurvivor`
 1. Generate a configuration file using `githubsurvivor-generate-config`
 2. Do an initial import of your bugs using `githubsurvivor-sync`
 3. Start the server using `githubsurvivor`

For detailed instructions, see
https://github.com/99designs/githubsurvivor/wiki/Installation


## Development notes

See https://github.com/99designs/githubsurvivor/wiki/Development

## License

MIT; see `LICENSE`


## Contributors

See https://github.com/99designs/githubsurvivor/wiki/Contributors


[1]: http://99designs.com
[2]: http://developer.github.com/v3/issues/
[3]: http://docs.atlassian.com/jira/REST/latest/
[4]: https://github.com/gengo/jirasurvivor
[5]: https://github.com/99designs/githubsurvivor/wiki/Backends
