# kv Library for hot person #

## Это моя типо библиотека) ##

## Какие функции имеются? ##
## НОВИНКА ##
 ## loadFileFromWebDav##
 `loadFileFromWebDav("webdav.yandex.ru", filepath, filename, login, password)` - берет название папки, название файла, логин(т е яндекс почта), и пароль от нее же, скачивает файлик этот !!
## chunk ##
`chunk(data, need_chanel,count_chanel=6, fs=250, )` - функция принимает датасет в формате [каналы все подрят][эпохи] и СПИСОК номеров нужных каналов, отдает только массив из нужных каналов. Count_chanel - общее количество каналов

    ![image](https://github.com/vladislava16062008/kv/assets/157376907/0f70d751-13b7-4ec3-a830-f1002079d5a1)

## read ##
`read(n)` - функция получает файлик dat с сигналами(кроме 8кк) возвращает массив с данными, массив со временем


##  f_spectrum ##
`f_spectrum(data,fre = 250)` - функция при принимает массив сигнала и возвращает 2 массива с частотами и амплитудами после преобразования Фурье

##  butter_bandpass ##
`butter_bandpass(data,lowcut, highcut, fs = 250, order=5)` - функция фильтра частот. Принимает массив, нижнюю границу, верхнюю границу. Отдает оббработанный массив 

## filt_kor ##
`filt_kor(s)` - функция фильтрации данных 8кк от Корецкого с финала. Принимает и отдает массив, фильтрует от 1 до 127


## chastots ##
`chastots(d,Fs = 250,save = False)` - функция получает массив, выводит картинку спектора фурье. Если save = True, то еще и массив с частотами


## pick ##
`pick(data,save = True)` - функция получает массив. Если save = True, то возвращает массив где есть пики, а если False, то колтчество пиков

## plt_pick ##
`plt_pick(d)` - функция принимает массив, выводит картинку с отмеченными пиками

## тг: @vladakumar ##
    


----------
