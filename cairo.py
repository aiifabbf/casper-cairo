#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""casper-cairo

a drawing backend for casper project, yet another Python binding for the 2D graphics library cairo.

- completely compatible with pycairo, while trying to provide any function that appears in cairo(yet not very useful for Python) but that does not in pycairo
- pure Python, using ctypes
- *planing* .ext for extensive use

Class and method descriptions are partly clipped from [official pycairo docs](http://cairographics.org/documentation/pycairo/3/reference), and additional information will be added at the end if necessary.

I took the constants from [ldo's qahirah](https://github.com/ldo/qahirah), which is the original pure Python binding for cairo and is the one that inspired me at first. But I felt quite uncomfortable to get too far away from pycairo, the official version of cairo's Python binding. So I decided to write one on my own.

I like the idea of pySDL2 putting extensive functions and classes in a separate package called .ext, but I am still not sure about whether I should make some extensions...what's the point?

Wooh, it's my first *practical* project!

Lots of thanks!

Benjamin Shi
2016/1/11
"""
import ctypes
import ctypes.util

try:
    _cairo = ctypes.CDLL(ctypes.util.find_library("cairo"))

except:
    raise Exception("libcairo*.so.* not found.")

# cairo_status_t
STATUS_SUCCESS = 0
STATUS_NO_MEMORY = 1
STATUS_INVALID_RESTORE = 2
STATUS_INVALID_POP_GROUP = 3
STATUS_NO_CURRENT_POINT = 4
STATUS_INVALID_MATRIX = 5
STATUS_INVALID_STATUS = 6
STATUS_NULL_POINTER = 7
STATUS_INVALID_STRING = 8
STATUS_INVALID_PATH_DATA = 9
STATUS_READ_ERROR = 10
STATUS_WRITE_ERROR = 11
STATUS_SURFACE_FINISHED = 12
STATUS_SURFACE_TYPE_MISMATCH = 13
STATUS_PATTERN_TYPE_MISMATCH = 14
STATUS_INVALID_CONTENT = 15
STATUS_INVALID_FORMAT = 16
STATUS_INVALID_VISUAL = 17
STATUS_FILE_NOT_FOUND = 18
STATUS_INVALID_DASH = 19
STATUS_INVALID_DSC_COMMENT = 20
STATUS_INVALID_INDEX = 21
STATUS_CLIP_NOT_REPRESENTABLE = 22
STATUS_TEMP_FILE_ERROR = 23
STATUS_INVALID_STRIDE = 24
STATUS_FONT_TYPE_MISMATCH = 25
STATUS_USER_FONT_IMMUTABLE = 26
STATUS_USER_FONT_ERROR = 27
STATUS_NEGATIVE_COUNT = 28
STATUS_INVALID_CLUSTERS = 29
STATUS_INVALID_SLANT = 30
STATUS_INVALID_WEIGHT = 31
STATUS_INVALID_SIZE = 32
STATUS_USER_FONT_NOT_IMPLEMENTED = 33
STATUS_DEVICE_TYPE_MISMATCH = 34
STATUS_DEVICE_ERROR = 35
STATUS_INVALID_MESH_CONSTRUCTION = 36
STATUS_DEVICE_FINISHED = 37
STATUS_JBIG2_GLOBAL_MISSING = 38
STATUS_LAST_STATUS = 39

# cairo_surface_type_t
SURFACE_TYPE_IMAGE = 0
SURFACE_TYPE_PDF = 1
SURFACE_TYPE_PS = 2
SURFACE_TYPE_XLIB = 3
SURFACE_TYPE_XCB = 4
SURFACE_TYPE_GLITZ = 5
SURFACE_TYPE_QUARTZ = 6
SURFACE_TYPE_WIN32 = 7
SURFACE_TYPE_BEOS = 8
SURFACE_TYPE_DIRECTFB = 9
SURFACE_TYPE_SVG = 10
SURFACE_TYPE_OS2 = 11
SURFACE_TYPE_WIN32_PRINTING = 12
SURFACE_TYPE_QUARTZ_IMAGE = 13
SURFACE_TYPE_SCRIPT = 14
SURFACE_TYPE_QT = 15
SURFACE_TYPE_RECORDING = 16
SURFACE_TYPE_VG = 17
SURFACE_TYPE_GL = 18
SURFACE_TYPE_DRM = 19
SURFACE_TYPE_TEE = 20
SURFACE_TYPE_XML = 21
SURFACE_TYPE_SKIA = 22
SURFACE_TYPE_SUBSURFACE = 23
SURFACE_TYPE_COGL = 24

# cairo_format_t
FORMAT_INVALID = -1
FORMAT_ARGB32 = 0
FORMAT_RGB24 = 1
FORMAT_A8 = 2
FORMAT_A1 = 3
FORMAT_RGB16_565 = 4
FORMAT_RGB30 = 5

# cairo_content_t
CONTENT_COLOR = 0x1000
CONTENT_COLOUR = 0x1000
CONTENT_ALPHA = 0x2000
CONTENT_COLOR_ALPHA = 0x3000
CONTENT_COLOUR_ALPHA = 0x3000

# cairo_extend_t
EXTEND_NONE = 0
EXTEND_REPEAT = 1
EXTEND_REFLECT = 2
EXTEND_PAD = 3

# cairo_filter_t
FILTER_FAST = 0
FILTER_GOOD = 1
FILTER_BEST = 2
FILTER_NEAREST = 3
FILTER_BILINEAR = 4
FILTER_GAUSSIAN = 5

# cairo_operator_t
OPERATOR_CLEAR = 0
OPERATOR_SOURCE = 1
OPERATOR_OVER = 2
OPERATOR_IN = 3
OPERATOR_OUT = 4
OPERATOR_ATOP = 5
OPERATOR_DEST = 6
OPERATOR_DEST_OVER = 7
OPERATOR_DEST_IN = 8
OPERATOR_DEST_OUT = 9
OPERATOR_DEST_ATOP = 10
OPERATOR_XOR = 11
OPERATOR_ADD = 12
OPERATOR_SATURATE = 13
OPERATOR_MULTIPLY = 14
OPERATOR_SCREEN = 15
OPERATOR_OVERLAY = 16
OPERATOR_DARKEN = 17
OPERATOR_LIGHTEN = 18
OPERATOR_COLOR_DODGE = 19
OPERATOR_COLOUR_DODGE = 19
OPERATOR_COLOR_BURN = 20
OPERATOR_COLOUR_BURN = 20
OPERATOR_HARD_LIGHT = 21
OPERATOR_SOFT_LIGHT = 22
OPERATOR_DIFFERENCE = 23
OPERATOR_EXCLUSION = 24
OPERATOR_HSL_HUE = 25
OPERATOR_HSL_SATURATION = 26
OPERATOR_HSL_COLOR = 27
OPERATOR_HSL_COLOUR = 27
OPERATOR_HSL_LUMINOSITY = 28

# cairo_antialias_t
ANTIALIAS_DEFAULT = 0
ANTIALIAS_NONE = 1
ANTIALIAS_GRAY = 2
ANTIALIAS_SUBPIXEL = 3
ANTIALIAS_FAST = 4
ANTIALIAS_GOOD = 5
ANTIALIAS_BEST = 6

#cairo_path_data_type
PATH_MOVE_TO = 0
PATH_LINE_TO = 1
PATH_CURVE_TO = 2
PATH_CLOSE_PATH = 3

class cairo_rectangle_t(ctypes.Structure):
    _fields_ = [
    ("x", ctypes.c_double), 
    ("y", ctypes.c_double), 
    ("width", ctypes.c_double), 
    ("height", ctypes.c_double)]

class cairo_rectangle_list_t(ctypes.Structure):
    _fields_ = [
    ("status", ctypes.c_int), 
    ("rectangles", ctypes.POINTER(cairo_rectangle_t)), 
    ("num_rectangles", ctypes.c_int)]

"""
typedef union _cairo_path_data_t cairo_path_data_t;
union _cairo_path_data_t {
    struct {
    cairo_path_data_type_t type;
    int length;
    } header;
    struct {
    double x, y;
    } point;
};
"""

class cairo_path_data_t(ctypes.Union):

    class header(ctypes.Structure):
        _fields_ = [
        ("type", ctypes.c_int), 
        ("length", ctypes.c_int)]

    class point(ctypes.Structure):
        _fields_ = [
        ("x", ctypes.c_double), 
        ("y", ctypes.c_double)]

class cairo_path_t(ctypes.Structure):
    _fields_ = [
    ("status", ctypes.c_int), 
    ("data", ctypes.POINTER(cairo_path_data_t)),
    ("num_data", ctypes.c_int)]

class cairo_font_extents_t(ctypes.Structure):
    _fields_ = [
    ("ascent", ctypes.c_double),
    ("descent", ctypes.c_double),
    ("height", ctypes.c_double),
    ("max_x_advance", ctypes.c_double),
    ("max_y_advance", ctypes.c_double)]

class Error(Exception): 
    """
    This exception is raised when a cairo object returns an error status.
    """
    pass

class Path:
    """
    Path cannot be instantiated directly, it is created by calling Context.copy_path() and Context.copy_path_flat().

    *It can be instantiated by _from_address().
    """
    def __init__(self):
        self._path_t = None

    @property
    def _as_parameter_(self):
        return self._path_t

    @classmethod
    def _from_address(cls, address):
        path = object.__new__(cls)
        path._path_t = ctypes.POINTER(cairo_path_t).from_address(address)
        return path

class Surface:
    """
    Surface is the abstract base class from which all the other surface classes derive. 

    It cannot be instantiated directly.

    *It can be instantiated by Surface._from_address() and casper-cairo will return a corresponding type(determined by _cairo.cairo_surface_get_type()) of surface.
    """

    def __init__(self):
        self._surface_t = None
        #self._as_parameter_ = self._surface_t

    @property
    def _as_parameter_(self):
        return self._surface_t

    #benjaminish
    @classmethod
    def _from_address(cls, address):
        """Get a specific Surface object from the given address

        This function uses cairo_surface_get_type() to determine the type of the cairo_surface_t and then transform them into a specific Python Surface type
        """
        surface = object.__new__(_surface_types[_cairo.cairo_surface_get_type(address)])
        surface._surface_t = address
        #surface._as_parameter_ = surface._surface_t
        return surface

    def copy_page(self):
        """
        Emits the current page for backends that support multiple pages, but doesn’t clear it, so that the contents of the current page will be retained for the next page. Use show_page() if you want to get an empty page after the emission.

        Origin:
        cairo.Surface.copy_page() in pycairo
        cairo_surface_copy_page() in cairo
        """
        _cairo.cairo_surface_copy_page(self._surface_t)

    def create_similar(self, content, width, height):
        """
        @param content: the CONTENT for the new surface
        @param width: width of the new surface, (in device-space units)
        @param height: height of the new surface (in device-space units)
        @return: a newly allocated Surface
        Create a Surface that is as compatible as possible with the existing surface. For example the new surface will have the same fallback resolution and FontOptions. Generally, the new surface will also use the same backend, unless that is not possible for some reason.

        *content is one of 

        Origin:
        cairo.Surface.create_similar() in pycairo
        cairo_surface_create_similar() in cairo
        """
        return Surface._from_address(_cairo.cairo_surface_create_similar(self._surface_t, content, width, height))

    def finish(self):
        """
        This method finishes the Surface and drops all references to external resources. For example, for the Xlib backend it means that cairo will no longer access the drawable, which can be freed. After calling finish() the only valid operations on a Surface are flushing and finishing it. Further drawing to the surface will not affect the surface but will instead trigger a cairo.Error exception.

        Origin:
        cairo.Surface.finish() in pycairo
        cairo_surface_finish() in cairo
        """
        _cairo.cairo_surface_finish(self._surface_t)

    def flush(self):
        """
        Do any pending drawing for the Surface and also restore any temporary modification’s cairo has made to the Surface’s state. This method must be called before switching from drawing on the Surface with cairo to drawing on it directly with native APIs. If the Surface doesn’t support direct access, then this function does nothing.

        Origin:
        cairo.Surface.flush() in pycairo
        cairo_surface_flush() in cairo
        """
        _cairo.cairo_surface_flush(self._surface_t)

    def get_content(self):
        """
        @return: The CONTENT type of Surface, which indicates whether the Surface contains color and/or alpha information.

        Origin:
        cairo.Surface.get_content() in pycairo
        cairo_surface_get_content() in cairo
        """
        return _cairo.cairo_surface_get_content(self._surface_t)

    def get_device_offset(self):
        """
        @return: (x_offset, y_offset) a tuple of float
            x_offset: the offset in the X direction, in device units
            y_offset: the offset in the Y direction, in device units

        Origin:
        cairo.Surface.get_device_offset() in pycairo
        cairo_surface_get_device_offset() in cairo
        """
        x_offset, y_offset = ctypes.c_double(), ctypes.c_double()
        _cairo.cairo_surface_get_device_offset(self._surface_t, ctypes.byref(x_offset), ctypes.byref(y_offset))
        return (x_offset.value, y_offset.value)

    def get_fallback_resolution(self):
        """
        @return: (x_pixels_per_inch, y_pixels_per_inch) a tuple of float
            x_pixels_per_inch: horizontal pixels per inch
            y_pixels_per_inch: vertical pixels per inch

        This method returns the previous fallback resolution set by set_fallback_resolution(), or default fallback resolution if never set.

        Origin:
        cairo.Surface.get_fallback_resolution() in pycairo
        cairo_surface_get_fallback_resolution() in cairo
        """
        x_pixels_per_inch, y_pixels_per_inch = ctypes.c_double(), ctypes.c_double()
        _cairo.cairo_surface_get_fallback_resolution(self._surface_t, ctypes.byref(x_pixels_per_inch), ctypes.byref(y_pixels_per_inch))
        return (x_pixels_per_inch.value, y_pixels_per_inch.value)

    def get_font_options(self):
        """
        @return: a FontOptions
        Retrieves the default font rendering options for the Surface. This allows display surfaces to report the correct subpixel order for rendering on them, print surfaces to disable hinting of metrics and so forth. The result can then be used with ScaledFont.

        Origin:
        cairo.Surface.get_font_options() in pycairo
        cairo_surface_get_font_options() in cairo
        """
        fontoptions = object.__new__(FontOptions)
        fontoptions._font_options_t = _cairo.cairo_surface_get_font_options(self._surface_t)
        #fontoptions._as_parameter_ = fontoptions._font_options_t
        return fontoptions

    def mark_dirty(self):
        """
        Tells cairo that drawing has been done to Surface using means other than cairo, and that cairo should reread any cached areas. Note that you must call flush() before doing such drawing.

        Origin:
        cairo.Surface.mark_dirty() in pycairo
        cairo_surface_mark_dirty() in cairo
        """
        _cairo.cairo_surface_mark_dirty(self._surface_t)

    def mark_dirty_rectangle(self, x, y, width, height):
        """
        @param x (int): – X coordinate of dirty rectangle
        @param y (int): – Y coordinate of dirty rectangle
        @param width (int): – width of dirty rectangle
        @param height (int): – height of dirty rectangle
        Like mark_dirty(), but drawing has been done only to the specified rectangle, so that cairo can retain cached contents for other parts of the surface.

        Any cached clip set on the Surface will be reset by this function, to make sure that future cairo calls have the clip set that they expect.

        Origin:
        cairo.Surface.mark_dirty_rectangle() in pycairo
        cairo_surface_mark_dirty_rectangle() in cairo
        """
        _cairo.cairo_surface_mark_dirty_rectangle(self._surface_t, x, y, width, height)

    def set_device_offset(self, x_offset, y_offset):
        """
        @param x_offset (float): – the offset in the X direction, in device units
        @param y_offset (float): – the offset in the Y direction, in device units
        Sets an offset that is added to the device coordinates determined by the CTM when drawing to Surface. One use case for this function is when we want to create a Surface that redirects drawing for a portion of an onscreen surface to an offscreen surface in a way that is completely invisible to the user of the cairo API. Setting a transformation via Context.translate() isn’t sufficient to do this, since functions like Context.device_to_user() will expose the hidden offset.

        Note that the offset affects drawing to the surface as well as using the surface in a source pattern.

        Origin:
        cairo.Surface.set_device_offset() in pycairo
        cairo_surface_set_device_offset() in cairo
        """
        _cairo.cairo_surface_set_device_offset(self._cairo_t, ctypes.c_double(x_offset), ctypes.c_double(y_offset))

    def set_fallback_resolution(self, x_pixels_per_inch, y_pixels_per_inch):
        """
        @param x_pixels_per_inch (float): – horizontal setting for pixels per inch
        @param y_pixels_per_inch (float): – vertical setting for pixels per inch
        Set the horizontal and vertical resolution for image fallbacks.

        When certain operations aren’t supported natively by a backend, cairo will fallback by rendering operations to an image and then overlaying that image onto the output. For backends that are natively vector-oriented, this function can be used to set the resolution used for these image fallbacks, (larger values will result in more detailed images, but also larger file sizes).

        Some examples of natively vector-oriented backends are the ps, pdf, and svg backends.

        For backends that are natively raster-oriented, image fallbacks are still possible, but they are always performed at the native device resolution. So this function has no effect on those backends.

        Note: The fallback resolution only takes effect at the time of completing a page (with Context.show_page() or Context.copy_page()) so there is currently no way to have more than one fallback resolution in effect on a single page.

        The default fallback resoultion is 300 pixels per inch in both dimensions.

        Origin:
        cairo.Surface.set_fallback_resolution() in pycairo
        cairo_surface_set_fallback_resolution() in cairo
        """
        _cairo.cairo_surface_set_fallback_resolution(self._cairo_t, ctypes.c_double(x_pixels_per_inch), ctypes.c_double(y_pixels_per_inch))

    def show_page(self):
        """
        Emits and clears the current page for backends that support multiple pages. Use copy_page() if you don’t want to clear the page.

        There is a convenience function for this that takes a Context.show_page().

        Origin:
        cairo.Surface.show_page() in pycairo
        cairo_surface_show_page() in cairo
        """
        _cairo.cairo_surface_show_page(self._cairo_t)

    def write_to_png(self, filename):
        """
        Writes the contents of Surface to fobj as a PNG image.

        Origin:
        cairo.Surface.write_to_png() in pycairo
        cairo_surface_write_to_png() in cairo (PNG-Support)

        *API conflict
        str, file or file-like object in pycairo
        while char* representing the filename only in cairo
        Taking cairo's way
        """
        ## pycairo's way is better
        _cairo.cairo_surface_write_to_png(self._cairo_t, filename)


class ImageSurface(Surface):
    """
    A cairo.ImageSurface provides the ability to render to memory buffers either allocated by cairo or by the calling code. The supported image formats are those defined in FORMAT attributes.
    """

    def __init__(self, format, width, height):
        """
        Creates an ImageSurface of the specified format and dimensions. Initially the surface contents are all 0. (Specifically, within each pixel, each color or alpha channel belonging to format will be 0. The contents of bits within a pixel, but not belonging to the given format are undefined).

        Origin:
        cairo.ImageSurface() in pycairo
        cairo_image_surface_create() in cairo
        """
        self._surface_t = _cairo.cairo_image_surface_create(format, width, height)
        #self._as_parameter_ = self._surface_t

    #benjaminish
    @classmethod
    def create_for_data(cls, data, format, width, height, stride):
        """
        @param cls: class
        @param data: data pointer(ctypes.c_char_p or simple an int representing the haed address)
        @param width (int): 
        @param height (int): 
        @param stride (int): 
        Creates an image surface for the provided pixel data. The output buffer must be kept around until the cairo_surface_t is destroyed or cairo_surface_finish() is called on the surface. The initial contents of data will be used as the initial image contents; you must explicitly clear the buffer, using, for example, cairo_rectangle() and cairo_fill() if you want it cleared.

        Note that the stride may be larger than width*bytes_per_pixel to provide proper alignment for each pixel and row. This alignment is required to allow high-performance rendering within cairo. The correct way to obtain a legal stride value is to call cairo_format_stride_for_width() with the desired format and maximum image width value, and then use the resulting stride value to allocate the data and to create the image surface. See cairo_format_stride_for_width() for example code.

        Origin:
        cairo.ImageSurface.create_for_data() in pycairo (though not available for now)
        cairo_image_surface_create_for_data() in cairo
        """
        surface = object.__new__(cls)
        surface._surface_t = _cairo.cairo_image_surface_create_for_data(data, format, width, height, stride)
        #surface._as_parameter_ = surface._surface_t
        return surface

    @classmethod
    def create_from_png(self, filename):
        """
        Creates a new image surface and initializes the contents to the given PNG file.

        Origin:
        cairo.ImageSurface.create_from_png() in pycairo
        cairo_image_surface_create_from_png() in cairo

        *API conflict
        str, file or file-like object in pycairo
        char* (representing filename) in cairo
        Take cairo's way for now
        """
        ## pycairo's way is more pythonic
        surface = object.__new__(cls)
        surface._surface_t = _cairo.cairo_image_surface_create_from_png(filename)
        return surface

    @staticmethod
    def format_stride_for_width(format, width):
        """
        This method provides a stride value that will respect all alignment requirements of the accelerated image-rendering code within cairo. 

        SEE ImageSurface.create_for_data()

        Since it's tied tightly to ImageSurface, this method surely becomes a staticmethod of ImageSurface.
        """
        return _cairo.cairo_format_stride_for_width(format, width)

    #benjaminish
    def get_data(self):
        """
        Get a pointer to the data of the image surface, for direct inspection or modification.

        A call to cairo_surface_flush() is required before accessing the pixel data to ensure that all pending drawing operations are finished. A call to cairo_surface_mark_dirty() is required after the data is modified.

        Origin:
        cairo.ImageSurface.get_data() in pycairo (yet not available, in docs, while available in the LATEST release)
        cairo_image_surface_get_data() in cairo
        """
        ## Still thinking about how to return a memoryview object which is more pythonic, though c_char_Array_* itself supports nearly everything a memoryview has.
        return (ctypes.c_char*(self.get_width()*self.get_height())).from_address(_cairo.cairo_image_surface_get_data(self._surface_t))

    def get_format(self):
        return _cairo.cairo_image_surface_get_format(self._surface_t)

    def get_height(self):
        return _cairo.cairo_image_surface_get_height(self._surface_t)

    def get_stride(self):
        return _cairo.cairo_image_surface_get_stride(self._surface_t)

    def get_width(self):
        return _cairo.cairo_image_surface_get_width(self._surface_t)


class Context:
    """
    Context is the main object used when drawing with cairo. To draw with cairo, you create a Context, set the target surface, and drawing options for the Context, create shapes with functions like Context.move_to() and Context.line_to(), and then draw shapes with Context.stroke() or Context.fill().

    Contexts can be pushed to a stack via Context.save(). They may then safely be changed, without loosing the current state. Use Context.restore() to restore to the saved state.
    """

    def __init__(self, target):
        """"
        Creates a new Context with all graphics state parameters set to default values and with target as a target surface. The target surface should be constructed with a backend-specific function such as ImageSurface (or any other cairo backend surface create variant).

        Origin:
        cairo.Context() in pycairo
        cairo_create() in cairo
        """
        try:
            self._cairo_t = _cairo.cairo_create(target._surface_t)
        except:
            raise Error("MemoryError: Insufficient memory.")
        self._as_parameter_ = self._cairo_t

    def append_path(self, path):
        """
        @param  path (Path object): to be appended
        Append the path onto the current path. The path may be either the return value from one of Context.copy_path() or Context.copy_path_flat() or it may be constructed manually (in C).

        Origin:
        cairo.Context.append_path() in pycairo
        cairo_append_path() in cairo
        """
        _cairo.cairo_append_path(path._path_t)

    def arc(self, xc, yc, radius, angle1, angle2):
        """
        @param xc (float): X position of the center of the arc
        @param yc (float): Y position of the center of the arc
        @param radius (float): the radius of the arc
        @param angle1 (float): the start angle, in radians
        @param angle2 (float): the end angle, in radians
        Adds a circular arc of the given radius to the current path. The arc is centered at (xc, yc), begins at angle1 and proceeds in the direction of increasing angles to end at angle2. If angle2 is less than angle1 it will be progressively increased by 2*PI until it is greater than angle1.

        If there is a current point, an initial line segment will be added to the path to connect the current point to the beginning of the arc. If this initial line is undesired, it can be avoided by calling Context.new_sub_path() before calling Context.arc().

        Angles are measured in radians. An angle of 0.0 is in the direction of the positive X axis (in user space). An angle of PI/2.0 radians (90 degrees) is in the direction of the positive Y axis (in user space). Angles increase in the direction from the positive X axis toward the positive Y axis. So with the default transformation matrix, angles increase in a clockwise direction.

        To convert from degrees to radians, use degrees * (math.pi / 180).

        This function gives the arc in the direction of increasing angles; see Context.arc_negative() to get the arc in the direction of decreasing angles.

        This function gives the arc in the direction of increasing angles; see Context.arc_negative() to get the arc in the direction of decreasing angles.

        The arc is circular in user space. To achieve an elliptical arc, you can scale the current transformation matrix by different amounts in the X and Y directions. For example, to draw an ellipse in the box given by x, y, width, height:

            ctx.save()
            ctx.translate(x + width / 2., y + height / 2.)
            ctx.scale(width / 2., height / 2.)
            ctx.arc(0., 0., 1., 0., 2 * math.pi)
            ctx.restore()

        Origin:
        cairo.Context.arc() in pycairo
        cairo_arc() in cairo
        """
        _cairo.cairo_arc(*[ctypes.c_double(i) for i in (xc, yc, radius, angle1, angle2)])

    def arc_negative(self, xc, yc, radius, angle1, angle2):
        """
        Adds a circular arc of the given radius to the current path. The arc is centered at (xc, yc), begins at angle1 and proceeds in the direction of decreasing angles to end at angle2. If angle2 is greater than angle1 it will be progressively decreased by 2*PI until it is less than angle1.

        See Context.arc() for more details. This function differs only in the direction of the arc between the two angles.

        Origin:
        cairo.Context.arc_negative() in pycairo
        cairo_arc_negative() in cairo
        """
        _cairo.cairo_arc(*[ctypes.c_double(i) for i in (xc, yc, radius, angle1, angle2)])

    def clip(self):
        """
        Establishes a new clip region by intersecting the current clip region with the current path as it would be filled by Context.fill() and according to the current FILL RULE (see Context.set_fill_rule()).

        After clip(), the current path will be cleared from the Context.

        The current clip region affects all drawing operations by effectively masking out any changes to the surface that are outside the current clip region.

        Calling clip() can only make the clip region smaller, never larger. But the current clip is part of the graphics state, so a temporary restriction of the clip region can be achieved by calling clip() within a Context.save()/Context.restore() pair. The only other means of increasing the size of the clip region is Context.reset_clip().

        Origin:
        cairo.Context.clip() in pycairo
        cairo_clip() in cairo
        """
        _cairo.cairo_clip(self._cairo_t)

    def clip_extents(self):
        """
        @return: (x1, y1, x2, y2)
        x1: left of the resulting extents
        y1: top of the resulting extents
        x2: right of the resulting extents
        y2: bottom of the resulting extents
        Computes a bounding box in user coordinates covering the area inside the current clip.

        Origin:
        cairo.Context.clip_extents() in pycairo
        cairo_clip_extents() in cairo
        """
        x1, y1, x2, y2 = [ctypes.c_double() for i in range(4)]
        _cairo.cairo_clip_extents(self._cairo_t, *[ctypes.byref(i) for i in (x1, y1, x2, y2)])
        return tuple(i.value for i in (x1, y1, x2, y2))

    def clip_preserve(self):
        """
        Establishes a new clip region by intersecting the current clip region with the current path as it would be filled by Context.fill() and according to the current FILL RULE (see Context.set_fill_rule()).

        Unlike Context.clip(), clip_preserve() preserves the path within the Context.

        The current clip region affects all drawing operations by effectively masking out any changes to the surface that are outside the current clip region.

        Calling clip_preserve() can only make the clip region smaller, never larger. But the current clip is part of the graphics state, so a temporary restriction of the clip region can be achieved by calling clip_preserve() within a Context.save()/Context.restore() pair. The only other means of increasing the size of the clip region is Context.reset_clip().

        Origin:
        cairo.Context.clip_preserve() in pycairo
        cairo_clip_preserve() in cairo
        """
        _cairo.cairo_clip_preserve(self._cairo_t)

    def close_path(self):
        """
        Adds a line segment to the path from the current point to the beginning of the current sub-path, (the most recent point passed to Context.move_to()), and closes this sub-path. After this call the current point will be at the joined endpoint of the sub-path.

        The behavior of close_path() is distinct from simply calling Context.line_to() with the equivalent coordinate in the case of stroking. When a closed sub-path is stroked, there are no caps on the ends of the sub-path. Instead, there is a line join connecting the final and initial segments of the sub-path.

        If there is no current point before the call to close_path(), this function will have no effect.

        Note: As of cairo version 1.2.4 any call to close_path() will place an explicit MOVE_TO element into the path immediately after the CLOSE_PATH element, (which can be seen in Context.copy_path() for example). This can simplify path processing in some cases as it may not be necessary to save the “last move_to point” during processing as the MOVE_TO immediately after the CLOSE_PATH will provide that point.

        Origin:
        cairo.Context.close_path() in pycairo
        cairo_close_path() in cairo
        """
        _cairo.cairo_close_path(self._cairo_t)

    def copy_clip_rectangle_list(self):
        """
        @return: list of tuple(x, y, width, height)
        float x: X coordinate of the left side of the rectangle
        float y: Y coordinate of the the top side of the rectangle
        float width: width of the rectangle
        float height: height of the rectangle

        Gets the current clip region as a list of rectangles in user coordinates. Never returns None.

        The status in the list may be STATUS_CLIP_NOT_REPRESENTABLE to indicate that the clip region cannot be represented as a list of user-space rectangles. The status may have other values to indicate other errors.

        Origin:
        cairo.Context.copy_clip_rectangle_list() in pycairo (yet not available)
        cairo_copy_clip_rectangle_list() in cairo
        """
        _cairo.cairo_copy_clip_rectangle_list.restype = ctypes.POINTER(cairo_rectangle_list_t)
        rectangle_list_t = _cairo.cairo_copy_clip_rectangle_list(self._cairo_t)
        rectangle_list = []
        for num in range(rectangle_list_t.contents.num_rectangles):
            i = rectangle_list_t.contents.rectangles[num]
            rectangle_list.append((i.x, i.y, i.width, i.height))
        return rectangle_list

    def copy_page(self):
        """
        Emits the current page for backends that support multiple pages, but doesn’t clear it, so, the contents of the current page will be retained for the next page too. Use Context.show_page() if you want to get an empty page after the emission.

        This is a convenience function that simply calls Surface.copy_page() on Context’s target.

        Origin:
        cairo.Context.copy_page() in pycairo
        cairo_copy_page() in cairo
        """
        _cairo.cairo_copy_page(self._cairo_t)

    def copy_path(self):
        """
        @return path (Path object)
        Creates a copy of the current path and returns it to the user as a Path. Raises MemoryError in case of no memory.

        Origin:
        cairo.Context.copy_path() in pycairo
        cairo_copy_path() in cairo
        """
        path = Path._from_address(_cairo.cairo_copy_path(self._cairo_t))
        if path._path_t.contents.status == STATUS_NO_MEMORY: raise Error("MemoryError: Insufficient memory.")
        return path

    def copy_path_flat(self):
        """
        Gets a flattened copy of the current path and returns it to the user as a Path.

        This function is like Context.copy_path() except that any curves in the path will be approximated with piecewise-linear approximations, (accurate to within the current tolerance value). That is, the result is guaranteed to not have any elements of type CAIRO_PATH_CURVE_TO which will instead be replaced by a series of PATH_LINE_TO elements.

        Origin:
        cairo.Context.copy_path_flat() in pycairo
        cairo_copy_path_flat() in cairo
        """
        path = Path._from_address(_cairo.cairo_copy_path_flat(self._cairo_t))
        if path._path_t.contents.status == STATUS_NO_MEMORY: raise Error("MemoryError: Insufficient memory.")
        return path

    def curve_to(self, x1, y1, x2, y2, x3, y3):
        """
        Adds a cubic Bézier spline to the path from the current point to position (x3, y3) in user-space coordinates, using (x1, y1) and (x2, y2) as the control points. After this call the current point will be (x3, y3).

        If there is no current point before the call to curve_to() this function will behave as if preceded by a call to ctx.move_to(x1, y1).

        Origin:
        cairo.Context.curve_to() in pycairo
        cairo_curve_to() in cairo
        """
        x1, y1, x2, y2, x3, y3 = [ctypes.c_double(i) for i in (x1, y1, x2, y2, x3, y3)]
        _cairo.cairo_curve_to(self._cairo_t, x1, y1, x2, y2, x3, y3)

    def fill(self):
        """
        A drawing operator that fills the current path according to the current FILL RULE, (each sub-path is implicitly closed before being filled). After fill(), the current path will be cleared from the Context. See Context.set_fill_rule() and Context.fill_preserve().
        """
        _cairo.cairo_fill(self._cairo_t)

    # benjaminish
    def fill_extents(self):
        """
        @return tuple(x1, y1, x2, y2)
        Computes a bounding box in user coordinates covering the area that would be affected, (the “inked” area), by a Context.fill() operation given the current path and fill parameters. If the current path is empty, returns an empty rectangle (0,0,0,0). Surface dimensions and clipping are not taken into account.

        Contrast with Context.path_extents(), which is similar, but returns non-zero extents for some paths with no inked area, (such as a simple line segment).

        Note that fill_extents() must necessarily do more work to compute the precise inked areas in light of the fill rule, so Context.path_extents() may be more desirable for sake of performance if the non-inked path extents are desired.

        See Context.fill(), Context.set_fill_rule() and Context.fill_preserve().
        """
        x1, y1, x2, y2 = [ctypes.c_double() for i in range(4)]
        _cairo.cairo_fill_extents(self._cairo_t, *[ctypes.byref(i) for i in (x1, y1, x2, y2)])
        return tuple(i.value for i in (x1, y1, x2, y2))

    def fill_preserve(self):
        """
        A drawing operator that fills the current path according to the current FILL RULE, (each sub-path is implicitly closed before being filled). Unlike Context.fill(), fill_preserve() preserves the path within the Context.

        See Context.set_fill_rule() and Context.fill().
        """
        _cairo.cairo_fill_preserve(self._cairo_t)

    def font_extents(self):
        """
        Gets the font extents for the currently selected font.
        """
        font_extents_t = cairo_font_extents_t()
        _cairo.cairo_font_extents(self._cairo_t, ctypes.byref(font_extents_t))
        return (font_extents_t.ascent, font_extents_t.descent, font_extents_t.height, font_extents_t.max_x_advance, font_extents_t.max_y_advance)

    def reference(self, cr):
        _cairo.cairo_reference(self._cairo_t)
        return self

    def destroy(self):
        pass

    def status(self):
        return _cairo.cairo_status(self._cairo_t)

    def save(self):
        _cairo.cairo_save(self._cairo_t)

    def restore(self):
        _cairo.cairo_restore(self._cairo_t)

    def get_target(self):
        return self.target

    def push_group(self):
        pass

    def push_group_to_source(self):
        pass

    def pop_group(self):
        pass

    def pop_group_to_source(self):
        pass

    def set_source_rgb(self, red, green, blue):
        _cairo.cairo_set_source_rgb(self._cairo_t, ctypes.c_double(red), ctypes.c_double(green), ctypes.c_double(blue))

    def set_source_rgba(self, red, green, blue, alpha):
        _cairo.cairo_set_source_rgba(self._cairo_t, ctypes.c_double(red), ctypes.c_double(green), ctypes.c_double(blue), ctypes.c_double(alpha))

    def set_source(self, source):
        _cairo.cairo_set_source(self._cairo_t, source._pattern_t)

    def set_source_surface(self, surface, x, y):
        _cairo.cairo_set_source_surface(self._cairo_t, surface._surface_t, x, y)

    def get_source(self):
        pattern = Pattern()
        pattern._pattern_t = _cairo.cairo_get_source(self._cairo_t)
        return pattern

    def set_antialias(self, antialis):
        _cairo.cairo_set_antialias(self._cairo_t, antialis)

    def get_antialise(self):
        return _cairo.cairo_get_antialias(self._cairo_t)

    def in_fill(self, x, y):
        return True if _cairo.cairo_in_fill(self._cairo_t, x, y) == 1 else False

    def mask(self, pattern):
        _cairo.cairo_mask(self._cairo_t, pattern._pattern_t)

    def paint(self):
        _cairo.cairo_paint(self._cairo_t)


_surface_types = {
    SURFACE_TYPE_IMAGE: ImageSurface,
    SURFACE_TYPE_PDF: None,
    SURFACE_TYPE_PS: None,
    SURFACE_TYPE_XLIB: None,
    SURFACE_TYPE_XCB: None,
    SURFACE_TYPE_GLITZ: None,
    SURFACE_TYPE_QUARTZ: None,
    SURFACE_TYPE_WIN32: None,
    SURFACE_TYPE_BEOS: None,
    SURFACE_TYPE_DIRECTFB: None,
    SURFACE_TYPE_SVG: None,
    SURFACE_TYPE_OS2: None,
    SURFACE_TYPE_WIN32_PRINTING: None,
    SURFACE_TYPE_QUARTZ_IMAGE: None,
    SURFACE_TYPE_SCRIPT: None,
    SURFACE_TYPE_QT: None,
    SURFACE_TYPE_RECORDING: None,
    SURFACE_TYPE_VG: None,
    SURFACE_TYPE_GL: None,
    SURFACE_TYPE_DRM: None,
    SURFACE_TYPE_TEE: None,
    SURFACE_TYPE_XML: None,
    SURFACE_TYPE_SKIA: None,
    SURFACE_TYPE_SUBSURFACE: None,
    SURFACE_TYPE_COGL: None,
}

if __name__ == "__main__":
    # testing
    s = ImageSurface(FORMAT_ARGB32, 100, 100)
    c = Context(s)
    c.set_source_rgba(0.5, 0.5, 0.5, 1)
    c.paint()
    a = s._from_address(s._surface_t)
