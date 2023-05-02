import abc
import logging
#import PySpin
logger = logging.getLogger(__name__)


class CameraModel(metaclass=abc.ABCMeta): # pylint: disable=too-many-public-methods
    """
    Abstract model that used to control the camera. Only one process can hold instance of this class for
    synchronization purpose. Ideally, the halo engine should not depend on a specific camera type. Any concrete camera
    model class should inherit this class and should have implemented the required functions.
    """
    @classmethod
    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'connect') and callable(subclass.connect) and hasattr(subclass, 'disconnect')
                and callable(subclass.disconnect) and hasattr(subclass, 'is_connected') and callable(
                    subclass.is_connected) and hasattr(subclass, 'next_frame') and callable(subclass.next_frame)
                and hasattr(subclass, 'get_auto_exposure_mode') and callable(subclass.get_auto_exposure_mode)
                and hasattr(subclass, 'set_auto_exposure_mode') and callable(subclass.set_auto_exposure_mode)
                and hasattr(subclass, 'get_exposure_time') and callable(subclass.get_exposure_time)
                and hasattr(subclass, 'set_exposure_time') and callable(subclass.set_exposure_time)
                and hasattr(subclass, 'get_auto_gain_mode') and callable(subclass.get_auto_gain_mode)
                and hasattr(subclass, 'set_auto_gain_mode') and callable(subclass.set_auto_gain_mode)
                and hasattr(subclass, 'get_gain') and callable(subclass.get_gain) and hasattr(subclass, 'set_gain')
                and callable(subclass.set_gain) and hasattr(subclass, 'get_trigger_mode')
                and callable(subclass.get_trigger_mode) and hasattr(subclass, 'set_trigger_mode')
                and callable(subclass.set_trigger_mode) and hasattr(subclass, 'get_trigger_source')
                and callable(subclass.get_trigger_source) and hasattr(subclass, 'set_trigger_source')
                and callable(subclass.set_trigger_source) and hasattr(subclass, 'get_image_format')
                and callable(subclass.get_image_format) and hasattr(subclass, 'set_image_format')
                and callable(subclass.set_image_format) and hasattr(subclass, 'acquisition_begin')
                and callable(subclass.acquisition_begin) and hasattr(subclass, 'acquisition_end')
                and callable(subclass.acquisition_end) and hasattr(subclass, 'get_acquisition_mode')
                and callable(subclass.get_acquisition_mode) and hasattr(subclass, 'set_acquisition_mode')
                and callable(subclass.set_acquisition_mode) and hasattr(subclass, 'get_stream_buffer_handling_mode')
                and callable(subclass.get_stream_buffer_handling_mode) and hasattr(
                    subclass, 'set_stream_buffer_handling_mode') and callable(subclass.set_stream_buffer_handling_mode)
                and hasattr(subclass, 'trigger') and callable(subclass.trigger) or NotImplemented)

    @abc.abstractmethod
    def get_auto_exposure_mode(self):
        """
        getter for auto exposure setting
        """
        raise NotImplementedError

    @abc.abstractmethod
    def set_auto_exposure_mode(self, value):
        """
        setter for auto exposure setting
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_exposure_time(self):
        """
        getter for exposure time setting
        """
        raise NotImplementedError

    @abc.abstractmethod
    def set_exposure_time(self, value):
        """
        setter for exposure time setting
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_auto_gain_mode(self):
        """
        getter for auto gain setting
        """
        raise NotImplementedError

    @abc.abstractmethod
    def set_auto_gain_mode(self, value):
        """
        setter for auto gain setting
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_gain(self):
        """
        getter for gain setting
        """
        raise NotImplementedError

    @abc.abstractmethod
    def set_gain(self, value):
        """
        setter for gain setting
        """
        raise NotImplementedError

    @abc.abstractmethod
    def connect(self):
        """
        connect the camera
        """
        raise NotImplementedError

    @abc.abstractmethod
    def disconnect(self):
        """
        disconnect the camera
        """
        raise NotImplementedError

    @abc.abstractmethod
    def is_connected(self):
        """
        check if the camera is connected
        """
        raise NotImplementedError

    @abc.abstractmethod
    def next_frame(self):
        """
        get the next from the camera buffer
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_trigger_mode(self):
        """
        getter for the trigger mode setting
        """
        raise NotImplementedError

    @abc.abstractmethod
    def set_trigger_mode(self, value):
        """
        setter for the trigger mode setting
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_trigger_delay(self):
        """
        getter for the trigger delay setting
        """
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_trigger_source(self):
        """
        getter for the trigger source setting
        """
        raise NotImplementedError

    @abc.abstractmethod
    def set_trigger_source(self, value):
        """
        setter for the trigger source setting
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_image_format(self):
        """
        getter for the image format setting
        """
        raise NotImplementedError

    @abc.abstractmethod
    def set_image_format(self, value):
        """
        setting for the image format setting
        """
        raise NotImplementedError

    @abc.abstractmethod
    def acquisition_begin(self):
        """
        tell the camera to begin the acquisition
        """
        raise NotImplementedError

    @abc.abstractmethod
    def acquisition_end(self):
        """
        tell the camera to end the acquisition
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_acquisition_mode(self):
        """
        getter for the acquisition mode setting
        """
        raise NotImplementedError

    @abc.abstractmethod
    def set_acquisition_mode(self, value):
        """
        setter for the acquisition mode setting
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_stream_buffer_handling_mode(self):
        """
        getter for the stream buffer handling mode setting
        """
        raise NotImplementedError

    @abc.abstractmethod
    def set_stream_buffer_handling_mode(self, value):
        """
        setter for the stream buffer handling mode setting
        """
        raise NotImplementedError

    @abc.abstractmethod
    def trigger(self):
        """
        tell the camera to trigger for the next acquisition
        """
        raise NotImplementedError

    AUTO_GAIN_MODE_OFF = 0
    AUTO_GAIN_MODE_CONTINUOUS = 1

    AUTO_EXPOSURE_MODE_OFF = 2
    AUTO_EXPOSURE_MODE_CONTINUOUS = 3

    TRIGGER_MODE_ON = 4
    TRIGGER_MODE_OFF = 5

    TRIGGER_SOURCE_SOFTWARE = 6
    TRIGGER_SOURCE_HARDWARE = 7

    PIXEL_FORMAT_BAYER_8 = 8
    PIXEL_FORMAT_BAYER_16 = 11
    PIXEL_FORMAT_BAYER_12_PACKED = 12
    PIXEL_FORMAT_BAYER_12_P = 13

    ACQUISITION_MODE_CONTINUOUS = 14
    ACQUISITION_MODE_SINGLE = 15
    ACQUISITION_MODE_MULTI = 16

    BUFFER_HANDLING_MODE_OLDEST_FIRST = 17
    BUFFER_HANDLING_MODE_OLDEST_FIRST_OVERWRITE = 18
    BUFFER_HANDLING_MODE_NEWEST_ONLY = 19
    BUFFER_HANDLING_MODE_NEWEST_FIRST = 20


class SyntheticCameraModel(CameraModel):  # pylint: disable=too-many-public-methods
    """
    A concrete camera model class that is specific to the camera, which support spinnaker driver.
    """
    def __init__(self):
        # image result
        self._image_result = None
        ## maybe: Declare synthetic image generator object here

        # 
        self._connected = False
        self._gain = 1.0            # need to tie this up with max_intensity in synthetic image generator
        self._exposure_time = 1     # need to tie this up with exposure in synthetic image generator
        self._acquisition_mode = CameraModel.ACQUISITION_MODE_SINGLE    # decides how synthetic image generator serializes the output
        self._image_format = CameraModel.PIXEL_FORMAT_BAYER_8           # decides how many bits synthetic image generates
        

    def connect(self):
        print("Connecting to Camera", ' Synthetic')
        ## maybe: Generate image here

        ## after image is generated
        return True

    def disconnect(self):
        ## maybe: Check of image generation is complete here
        return True

    def is_connected(self):
        return True

    def get_auto_gain_mode(self):
        return CameraModel.AUTO_GAIN_MODE_OFF

    def set_auto_gain_mode(self, value):
        if value == CameraModel.AUTO_GAIN_MODE_OFF:
            return True
        else:
            raise Exception('No Other gain modes implemented yet')

    def get_gain(self):
        ## maybe maintain gain variable for controlling brightness
        return self._gain    #self._cam.Gain.GetValue()

    def set_gain(self, value):
        val_gain_min = 0              # get from synthetic image generator
        val_gain_max = 50               

        val_gain_set = max(val_gain_min, value)
        val_gain_set = min(val_gain_max, val_gain_set)
        
        self._gain = val_gain_set
        return True

    def get_auto_exposure_mode(self):
        return CameraModel.AUTO_EXPOSURE_MODE_OFF

    def set_auto_exposure_mode(self, value):
        if value == CameraModel.AUTO_EXPOSURE_MODE_OFF:
            return True
        else:
            raise Exception('No Other exposure modes implemented yet')

    def get_exposure_time(self):
        return self._exposure_time

    def set_exposure_time(self, value):
        val_exposure_min = 1            # must come from synthetic image generator
        val_exposure_max = 1000
        val_exposure_set = max(val_exposure_min, value)
        val_exposure_set = min(val_exposure_max, val_exposure_set)
        self._exposure_time = val_exposure_set
        return True

    def get_stream_buffer_handling_mode(self):
        return CameraModel.BUFFER_HANDLING_MODE_NEWEST_ONLY

    def set_stream_buffer_handling_mode(self, value):
        if value == CameraModel.BUFFER_HANDLING_MODE_NEWEST_ONLY:
            return True
        else:
            raise Exception('No Other buffer handling modes implemented yet')

    def get_acquisition_mode(self):
        return CameraModel.ACQUISITION_MODE_SINGLE

    def set_acquisition_mode(self, value):
        if value == CameraModel.ACQUISITION_MODE_SINGLE:
            self._acquisition_mode = value
            return True

    def acquisition_begin(self):
        ## maybe: Generate image here

        ## after image is generated
        return True
        
    def acquisition_end(self):
        ## maybe release self._image_result
        #self._image_result.Release()
        #self._image_result = None
        return True
        
    def next_frame(self):
        try:
            if self._image_result is not None:
                # release the old image from the buffer
                self._image_result.Release()
                self._image_result = None

            # get next image from the buffer
            self._image_result = self._cam.GetNextImage(1000)

            if self._image_result.IsIncomplete():
                logger.info('Image incomplete with image status %d ...', self._image_result.GetImageStatus())
                return None

            # Getting the image data as a numpy array
            return self._image_result.GetNDArray()

        except PySpin.SpinnakerException as ex:
            logger.info('Error: %s', ex)
            return None

    def get_trigger_mode(self):
        return CameraModel.TRIGGER_MODE_ON

    def set_trigger_mode(self, value):
        return True

    def get_trigger_delay(self):
        return 1        # don't want to make it zero yet, so it wouldn't break halovision
        
    def get_trigger_source(self):
        return CameraModel.TRIGGER_SOURCE_SOFTWARE

    def set_trigger_source(self, value):
        return True

    def get_image_format(self):
        return self._image_format

    def set_image_format(self, value):
        if value == CameraModel.PIXEL_FORMAT_BAYER_8:
            self._image_format = value                          
            return True
        else:
            raise Exception('No other image format is implemented yet')
        
    def trigger(self):
        return True


def main():
    cam_model: CameraModel = SyntheticCameraModel()
    print(f'''
                connect: {cam_model.connect()}
                is_connected: {cam_model.is_connected()}
                set_auto_gain_mode: {cam_model.set_auto_gain_mode(CameraModel.AUTO_GAIN_MODE_OFF)}
                get_auto_gain_mode: {cam_model.get_auto_gain_mode()}
                set_gain: {cam_model.set_gain(2.0)}
                get_gain: {cam_model.get_gain()}
                set_auto_exposure_mode: {cam_model.set_auto_exposure_mode(CameraModel.AUTO_EXPOSURE_MODE_OFF)}
                get_auto_exposure_mode: {cam_model.get_auto_exposure_mode()}
                set_exposure_time: {cam_model.set_exposure_time(5)}
                get_exposure_time: {cam_model.get_exposure_time()}
                set_stream_buffer_handling_mode: {cam_model.set_stream_buffer_handling_mode(CameraModel.BUFFER_HANDLING_MODE_NEWEST_ONLY)}
                get_stream_buffer_handling_mode: {cam_model.get_stream_buffer_handling_mode()}
                set_aquisition_mode: {cam_model.set_acquisition_mode(CameraModel.ACQUISITION_MODE_SINGLE)}
                get_aquisition_mode: {cam_model.get_acquisition_mode()}
                set_trigger_mode: {cam_model.set_trigger_mode(CameraModel.TRIGGER_MODE_ON)}
                get_trigger_mode: {cam_model.get_trigger_mode()}
                set_trigger_source: {cam_model.set_trigger_source(CameraModel.TRIGGER_SOURCE_SOFTWARE)}
                get_trigger_source: {cam_model.get_trigger_source()}
                get_trigger_delay: {cam_model.get_trigger_delay()}
                set_image_format: {cam_model.set_image_format(CameraModel.PIXEL_FORMAT_BAYER_8)}
                get_image_format: {cam_model.get_image_format()}
                acquisition_begin: {cam_model.acquisition_begin()}

                trigger: {cam_model.trigger()}
                next_frame: {cam_model.next_frame()}

                acquisition_end: {cam_model.acquisition_end()}
                disconnect: {cam_model.disconnect()}
                
    ''')
    

if __name__ == '__main__':
    import os
    os.system('clear')
    main()