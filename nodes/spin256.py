class Spin256SizeSelector:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "index": ("INT", {"default": 0, "min": 0, "max": 9, "step": 1}),
                "size_0": ("STRING", {"default": "848,480"}),
                "size_1": ("STRING", {"default": "1280,720"}),
                "size_2": ("STRING", {"default": "1920,1080"}),
                "size_3": ("STRING", {"default": "0,0"}),
                "size_4": ("STRING", {"default": "0,0"}),
                "size_5": ("STRING", {"default": "0,0"}),
                "size_6": ("STRING", {"default": "0,0"}),
                "size_7": ("STRING", {"default": "0,0"}),
                "size_8": ("STRING", {"default": "0,0"}),
                "size_9": ("STRING", {"default": "0,0"}),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "pick"
    CATEGORY = "Spin256"

    def pick(self, index, size_0, size_1, size_2, size_3, size_4, size_5, size_6, size_7, size_8, size_9):
        sizes = [size_0, size_1, size_2, size_3, size_4, size_5, size_6, size_7, size_8, size_9]
        index = max(0, min(index, len(sizes) - 1))
        try:
            w, h = [int(x.strip()) for x in sizes[index].split(",")]
        except Exception:
            w, h = 1280, 720
        return (w, h)

class Spin256IntSelector:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "index": ("INT", {"default": 0, "min": 0, "max": 9, "step": 1}),
                "int_0": ("INT", {"default": 0}),
                "int_1": ("INT", {"default": 0}),
                "int_2": ("INT", {"default": 0}),
                "int_3": ("INT", {"default": 0}),
                "int_4": ("INT", {"default": 0}),
                "int_5": ("INT", {"default": 0}),
                "int_6": ("INT", {"default": 0}),
                "int_7": ("INT", {"default": 0}),
                "int_8": ("INT", {"default": 0}),
                "int_9": ("INT", {"default": 0}),
            }
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "pick"
    CATEGORY = "Spin256"

    def pick(self, index, int_0, int_1, int_2, int_3, int_4, int_5, int_6, int_7, int_8, int_9):
        sizes = [int_0, int_1, int_2, int_3, int_4, int_5, int_6, int_7, int_8, int_9]
        index = max(0, min(index, len(sizes) - 1))
        return (sizes[index],)
        
class Spin256StringSelector:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "index": ("INT", {"default": 0, "min": 0, "max": 9, "step": 1}),
                "str_0": ("STRING", {"default": ""}),
                "str_1": ("STRING", {"default": ""}),
                "str_2": ("STRING", {"default": ""}),
                "str_3": ("STRING", {"default": ""}),
                "str_4": ("STRING", {"default": ""}),
                "str_5": ("STRING", {"default": ""}),
                "str_6": ("STRING", {"default": ""}),
                "str_7": ("STRING", {"default": ""}),
                "str_8": ("STRING", {"default": ""}),
                "str_9": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "pick"
    CATEGORY = "Spin256"

    def pick(self, index, str_0, str_1, str_2, str_3, str_4, str_5, str_6, str_7, str_8, str_9):
        sizes = [str_0, str_1, str_2, str_3, str_4, str_5, str_6, str_7, str_8, str_9]
        index = max(0, min(index, len(sizes) - 1))
        return (sizes[index],)

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
