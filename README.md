# pytest-power

![python](https://github.com/NL-ix/pytest-power/workflows/python/badge.svg)
[![PyPI](https://img.shields.io/pypi/v/pytest-power?style=flat)](https://pypi.org/project/pytest-power/)

Adds a number of shorthands for fixtures and other helpers for easier testing:

- patch.object
- patch.init
- patch.many
- patch.everything

You can instal pytest-power with pip:

```sh
pip install pytest-power
```

## Usage

### patch.object

A shorthand for pytest-mock's `mocker.patch.object`


```python
from myapp import App

def test_app_run(patch):
  patch.object(App, 'run')
  App.run()
  assert App.run.call_count == 1
```

You can pass keywords arguments as usual:

```python
from myapp import App

def test_app_run(patch):
  patch.object(App, 'run', return_value='running')
  assert App.run() == 'running'
```


### patch.init

Makes patching `__init__` a bit simpler:


```python
from myapp import App

def test_app_init(patch):
  patch.init(App)
  app = App()
  assert isinstance(app, App)
```

Instances patched in this way do not have properties that are set in `__init__`,
so they have to be set again by hand.

Keyword arguments are passed to underlying `patch.object`, and autospec is
enabled by default.


### patch.many

A shorthand to patch many properties of the same object:

```python
from myapp import App

def test_app_run_called_by_run(patch):
  patch.many(App, ['run', 'called_by_run'])
  App.run()
  assert App.called_by_run.call_count == 1
```

Keyword arguments are again passed to underlying `patch.object`, and autospec
is enabled by default.

### patch.everything

A shorthand to patch every non-magic property. Useful when patch.many gets
too long!

```python
from myapp import App


def test_app_run_called_by_run(patch):
  patch.everything(App)
  App.run()
  assert App.called_by_run.call_count == 1
```

Supports forcing the exclusion of properties:

```python
from myapp import App


def test_app_run(patch, excludes=['run']):
  patch.everything(App)
  App.run()
  assert App.called_by_run.call_count == 1
```


And forcing the inclusion of properties:

```python
from myapp import App


def test_app_run(patch, includes=['__private__']):
  patch.everything(App)
  App.run()
  assert App.__private__.call_count == 1
```
