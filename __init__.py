from .nodes.cascades import NODE_CLASS_MAPPINGS as CASCADES_NODE_CLASS_MAPPINGS
from .nodes.cascades import NODE_DISPLAY_NAME_MAPPINGS as CASCADES_NODE_DISPLAY_NAME_MAPPINGS
from .nodes.code import NODE_CLASS_MAPPINGS as CODE_NODE_CLASS_MAPPINGS
from .nodes.code import NODE_DISPLAY_NAME_MAPPINGS as CODE_NODE_DISPLAY_NAME_MAPPINGS
from .nodes.luts import NODE_CLASS_MAPPINGS as LUTS_NODE_CLASS_MAPPINGS
from .nodes.luts import NODE_DISPLAY_NAME_MAPPINGS as LUTS_NODE_DISPLAY_NAME_MAPPINGS
from .nodes.waifu2x import NODE_CLASS_MAPPINGS as WAIFU2X_NODE_CLASS_MAPPINGS
from .nodes.waifu2x import NODE_DISPLAY_NAME_MAPPINGS as WAIFU2X_NODE_DISPLAY_NAME_MAPPINGS

WEB_DIRECTORY = "./web"
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

# Cascades
NODE_CLASS_MAPPINGS.update(CASCADES_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(CASCADES_NODE_DISPLAY_NAME_MAPPINGS)
print(f'\033[93m[Shibiko AI] \033[31mCascades \033[92mLoaded\033[0m')

# Code
NODE_CLASS_MAPPINGS.update(CODE_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(CODE_NODE_DISPLAY_NAME_MAPPINGS)
print(f'\033[93m[Shibiko AI] \033[31mCode \033[92mLoaded\033[0m')

# Luts
NODE_CLASS_MAPPINGS.update(LUTS_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(LUTS_NODE_DISPLAY_NAME_MAPPINGS)
print(f'\033[93m[Shibiko AI] \033[31mLuts \033[92mLoaded\033[0m')

# Waifu2x
NODE_CLASS_MAPPINGS.update(WAIFU2X_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(WAIFU2X_NODE_DISPLAY_NAME_MAPPINGS)
print(f'\033[93m[Shibiko AI] \033[31mWaifu2x \033[92mLoaded\033[0m')

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']
print(f'\033[93m[Shibiko AI] \033[92mLoading Complete!\033[0m')
