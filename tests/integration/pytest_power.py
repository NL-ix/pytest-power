# -*- coding: utf-8 -*-
import json
import os
from pathlib import Path
from unittest.mock import MagicMock

from pytest import raises


def test_magic(mocker, magic):
    assert magic == MagicMock


def test_patch_init(patch_init):
    patch_init(Path)
    Path('path')
    Path.__init__.assert_called_with('path')


def test_patch_init__kwargs(patch_init):
    patch_init(Path, key='value')


def test_patch_many(patch_many):
    patch_many(os, ['open'])
    os.open('open')
    os.open.assert_called_with('open')


def test_patch_many__autospec(patch_many):
    patch_many(os, ['open'])
    os.open('open')
    with raises(AttributeError):
        os.open.whatever('open')


def test_patch_many__autospec_false(patch_many):
    patch_many(os, ['open'], autospec=False)
    os.open('open')
    assert os.open.whatever('open')


def test_patch_many__kwargs(patch_many):
    patch_many(os, ['open'], key='value')


def test_patch_everything(patch_everything):
    patch_everything(json)
    assert isinstance(json.dumps('whatever'), MagicMock)
    assert isinstance(json.loads('whatever'), MagicMock)
    assert not isinstance(json.__doc__, MagicMock)
    assert not isinstance(json.__builtins__, MagicMock)


def test_patch_everything__autospec_false(patch_everything):
    patch_everything(json, autospec=False)
    assert isinstance(json.dumps('too', 'much', 'stuff'), MagicMock)


def test_patch_everything__excludes(patch_everything):
    patch_everything(json, excludes=['_default_decoder', 'loads', 'decoder'])
    with raises(json.decoder.JSONDecodeError):
        json.loads('whatever')


def test_patch(patch, patch_init, patch_many, patch_everything):
    assert patch.init == patch_init
    assert patch.many == patch_many
    assert patch.everything == patch_everything
