from typing import assert_type

import pytest

import calculate


def test_calc_successor():
    # given
    funcs = calculate.funcs
    figs = calculate.figs
    sizes = {
        "area-circle": [5],
        "perimeter-circle": [5],
        "area-square": [4],
        "perimeter-square": [4]
    }
    results = []

    # when
    for fig in figs:
        for func in funcs:
            size_key = f"{func}-{fig}"
            size = sizes[size_key]
            results.append(calculate.calc(fig, func, size))

    # then
    for result in results:
        assert isinstance(result, (int, float))


def test_calc_invalid_figure():
    # given
    fig = 'invalid-figure'
    func = 'area'
    size = [3]

    # when and then
    with pytest.raises(AssertionError):
        calculate.calc(fig, func, size)


def test_calc_invalid_function():
    # given
    fig = 'square'
    func = 'invalid-function'
    size = [3]

    # when and then
    with pytest.raises(AssertionError):
        calculate.calc(fig, func, size)


def test_calc_invalid_size():
    # given

    fig = 'square'
    func = 'area'
    size = ["wrong"]

    # when and then
    with pytest.raises(TypeError):
        calculate.calc(fig, func, size)


def test_calc_invalid_size_key():
    # given
    fig = 'square'
    func = 'area'
    size = [1, 2]

    # when and then
    with pytest.raises(TypeError):
        calculate.calc(fig, func, size)
