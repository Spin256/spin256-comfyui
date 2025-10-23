from .nodes.spin256 import *


NODE_CLASS_MAPPINGS = {
    "Spin256SizeSelector": Spin256SizeSelector, 
    "Spin256IntSelector": Spin256IntSelector, 
    "Spin256StringSelector": Spin256StringSelector
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "Spin256SizeSelector": "Size Selector",
    "Spin256IntSelector":"Int Selector" ,
    "Spin256StringSelector":"String Selector"
}
