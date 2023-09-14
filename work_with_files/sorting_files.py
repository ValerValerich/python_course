import os


def sorting_file(way):
    ls_dir = os.listdir(way)
    ext_text = ['txt', 'doc']
    ext_jpg = ['jpg', 'jpeg', 'gif']
    ext_video = ['avi', 'mp4']
    for el in ls_dir:
        lst_file = el.split('.')
        if len(lst_file) > 1:
            if lst_file[-1] in ext_text:
                os.mkdir(os.path.join(way, 'text'))
                os.replace(os.path.join(way, el), os.path.join(way, 'text', el))
            if lst_file[-1] in ext_jpg:
                os.mkdir(os.path.join(way, 'images'))
                os.replace(os.path.join(way, el), os.path.join(way, 'images', el))
            if lst_file[-1] in ext_video:
                os.mkdir(os.path.join(way, 'video'))
                os.replace(os.path.join(way, el), os.path.join(way, 'video', el))

