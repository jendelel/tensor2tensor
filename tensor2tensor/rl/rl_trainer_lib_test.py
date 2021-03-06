# coding=utf-8
# Copyright 2018 The Tensor2Tensor Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests of basic flow of collecting trajectories and training PPO."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensor2tensor.data_generators.gym_problems import standard_atari_env_spec
from tensor2tensor.models.research.rl import simple_gym_spec
from tensor2tensor.rl import rl_trainer_lib
from tensor2tensor.utils import registry  # pylint: disable=unused-import
from tensor2tensor.utils import trainer_lib

import tensorflow as tf


class TrainTest(tf.test.TestCase):

  test_config = ("epochs_num=4,eval_every_epochs=3,video_during_eval=False,"
                 "num_agents=5,optimization_epochs=5,epoch_length=50")

  def test_no_crash_pendulum(self):
    hparams = trainer_lib.create_hparams(
        "ppo_continuous_action_base",
        TrainTest.test_config)

    hparams.add_hparam("environment_spec", simple_gym_spec("Pendulum-v0"))
    rl_trainer_lib.train(hparams)

  def test_no_crash_cartpole(self):
    hparams = trainer_lib.create_hparams(
        "ppo_discrete_action_base",
        TrainTest.test_config)

    hparams.add_hparam("environment_spec",
                       standard_atari_env_spec("CartPole-v0"))
    rl_trainer_lib.train(hparams)


if __name__ == "__main__":
  tf.test.main()
