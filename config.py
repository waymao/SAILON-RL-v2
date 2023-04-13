from obs_convertion import LidarAll, OnlyFacingObs, OnlyHinted
import tianshou as ts
from policies import BiasedDQN
from net.basic import BasicNet
from net.norm_net import NormalizedNet

OBS_TYPES = {
    "lidar_all": LidarAll,
    "only_facing": OnlyFacingObs,
    "only_hinted": OnlyHinted,
}

NOVELTIES = {
    "mi": "novelties/evaluation1/multi_interact/multi_interact.json",
    "kibt": "novelties/evaluation1/key_inventory_break_tree/key_inventory_break_tree.json",
    "rdb": "novelties/evaluation1/random_drop_break/random_drop_break.json",
    "space_ar": "novelties/evaluation1/space_around_crafting_table/space_around_crafting_table.json",
}

POLICIES = {
    "dqn": ts.policy.DQNPolicy,
    "novel_boost": BiasedDQN
}

POLICY_PROPS = {
    "dqn": {},
    "novel_boost": {
        "novel_boost": 2
    }
}


HINTS = {
    "mi": "",
    "kibt": str([
        "Sorry, you need a key to trade with me.",
        "(trade_block_of_titanium_1)"
    ]),
    "rdb": "",
    "space_ar": "",
}


RL_ALGOS = {
    "dqn": ts.policy.DQNPolicy,
}

NETS = {
    "basic": BasicNet,
    "normalized": NormalizedNet,
}

REWARDS = {
    "positive": 1000,
    "negative": -250,
    "step": -1,
}
