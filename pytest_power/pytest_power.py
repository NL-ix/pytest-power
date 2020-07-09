# -*- coding: utf-8 -*-
from pytest import fixture

from .utils import Utils


@fixture
def magic(mocker):
    """
    Shorthand for mocker.MagicMock. It's magic!
    """
    return mocker.MagicMock


@fixture
def patch_init(mocker):
    """
    Makes patching a class' constructor slightly easier
    """
    def patch_init(item, **kwargs):
        mocker.patch.object(item, '__init__', return_value=None, **kwargs)
    return patch_init


@fixture
def patch_many(mocker):
    """
    Makes patching many attributes of the same object simpler
    """
    def patch_many(item, attributes, autospec=True, **kwargs):
        for attribute in attributes:
            mocker.patch.object(item, attribute, autospec=autospec, **kwargs)
    return patch_many


@fixture
def patch_everything(mocker):
    """
    Patches every attribute of an object.
    """
    def patch_everything(item, autospec=True, excludes=None, includes=None):
        for attribute in Utils.patchable_attributes(item, excludes=excludes,
                                                    includes=includes):
            mocker.patch.object(item, attribute, autospec=autospec)
    return patch_everything


@fixture
def patch(mocker, patch_init, patch_many, patch_everything):
    mocker.patch.init = patch_init
    mocker.patch.many = patch_many
    mocker.patch.everything = patch_everything
    return mocker.patch
