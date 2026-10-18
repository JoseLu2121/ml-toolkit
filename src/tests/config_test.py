from ml_toolkit.config import ExperimentConfig
import pytest
from typing import Any

def test_lr():
    with pytest.raises(ValueError):
        ExperimentConfig("test_lr_negative", lr = -1.0)

    with pytest.raises(ValueError):
        ExperimentConfig("test_lr_zero", lr = 0.0)

    assert ExperimentConfig("test_lr_positive").lr > 0.0

def test_batch_size():
    with pytest.raises(ValueError):
        ExperimentConfig("test_bs_negative", batch_size = -1.0)

    with pytest.raises(ValueError):
        ExperimentConfig("test_bs_zero", batch_size = 0.0)

    assert ExperimentConfig("test_bs_positive").batch_size > 0.0


def test_epochs():
    with pytest.raises(ValueError):
        ExperimentConfig("test_bs_negative", epochs = -1.0)

    with pytest.raises(ValueError):
        ExperimentConfig("test_bs_zero", epochs = 0.0)

    assert ExperimentConfig("test_bs_positive").epochs > 0.0

def test_name():
    with pytest.raises(ValueError):
        ExperimentConfig("")

def test_wrong_name_in_dict():
    mock_wrong_name: ExperimentConfig = ExperimentConfig.from_dict({"name" : "test_dict", "wrong_name" : 1.0})

    d: dict[str, Any] =  mock_wrong_name.to_dict()
    assert "name" in d
    assert not "wrong_name" in d