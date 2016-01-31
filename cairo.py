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

_cairo_dll = ctypes.util.find_library("cairo")
if not _cairo_dll: raise Exception("libcairo not found.")

try:
    _cairo = ctypes.CDLL(_cairo_dll)

except:
    raise Exception("Failed to load libcairo.")

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

# cairo_line_cap_t
LINE_CAP_BUTT = 0
LINE_CAP_ROUND = 1
LINE_CAP_SQUARE = 2

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

# cairo_subpixel_order_t
SUBPIXEL_ORDER_DEFAULT = 0
SUBPIXEL_ORDER_RGB = 1
SUBPIXEL_ORDER_BGR = 2
SUBPIXEL_ORDER_VRGB = 3
SUBPIXEL_ORDER_VBGR = 4

# cairo_hint_style_t
HINT_STYLE_DEFAULT = 0
HINT_STYLE_NONE = 1
HINT_STYLE_SLIGHT = 2
HINT_STYLE_MEDIUM = 3
HINT_STYLE_FULL = 4

# cairo_hint_metrics_t
HINT_METRICS_DEFAULT = 0
HINT_METRICS_OFF = 1
HINT_METRICS_ON = 2

#cairo_path_data_type
PATH_MOVE_TO = 0
PATH_LINE_TO = 1
PATH_CURVE_TO = 2
PATH_CLOSE_PATH = 3

# cairo_fill_rule_t
FILL_RULE_WINDING = 0
FILL_RULE_EVEN_ODD = 1

# cairo_line_join_t
LINE_JOIN_MITER = 0
LINE_JOIN_MITRE = 0
LINE_JOIN_ROUND = 1
LINE_JOIN_BEVEL = 2

# cairo_font_type_t
FONT_TYPE_TOY = 0
FONT_TYPE_FT = 1
FONT_TYPE_WIN32 = 2
FONT_TYPE_QUARTZ = 3
FONT_TYPE_USER = 4

# cairo_font_slant_t
FONT_SLANT_NORMAL = 0
FONT_SLANT_ITALIC = 1
FONT_SLANT_OBLIQUE = 2

# cairo_font_weight_t
FONT_WEIGHT_NORMAL = 0
FONT_WEIGHT_BOLD = 1

# cairo_pattern_type_t
PATTERN_TYPE_SOLID = 0
PATTERN_TYPE_SURFACE = 1
PATTERN_TYPE_LINEAR = 2
PATTERN_TYPE_RADIAL = 3
PATTERN_TYPE_MESH = 4
PATTERN_TYPE_RASTER_SOURC = 5

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

# I write only those Structures that are essential to my implementing all the functionalities.
class cairo_path_data_t(ctypes.Union):

    class header(ctypes.Structure):
        _fields_ = [
        ("type", ctypes.c_int), 
        ("length", ctypes.c_int)]

    class point(ctypes.Structure):
        _fields_ = [
        ("x", ctypes.c_double), 
        ("y", ctypes.c_double)]

    _fields_ = [
    ("header", header),
    ("point", point)]

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

class cairo_text_extents_t(ctypes.Structure):
    _fields_ = [
    ("x_bearing", ctypes.c_double),
    ("y_bearing", ctypes.c_double),
    ("width", ctypes.c_double),
    ("height", ctypes.c_double),
    ("x_advance", ctypes.c_double),
    ("y_advance", ctypes.c_double)]

class cairo_matrix_t(ctypes.Structure):
    _fields_ = [
    ("xx", ctypes.c_double),
    ("yx", ctypes.c_double),
    ("xy", ctypes.c_double),
    ("yy", ctypes.c_double),
    ("x0", ctypes.c_double),
    ("y0", ctypes.c_double)]

class cairo_glyph_t(ctypes.Structure):
    _fields_ = [
    ("index", ctypes.c_ulong),
    ("x", ctypes.c_double),
    ("y", ctypes.c_double)]

cairo_write_func_t = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)

cairo_read_func_t = cairo_write_func_t

class Error(Exception): 
    """
    This exception is raised when a cairo object returns an error status.
    """
    pass

class Matrix:
    """
    Matrix is used throughout cairo to convert between different coordinate spaces. A Matrix holds an affine transformation, such as a scale, rotation, shear, or a combination of these. The transformation of a point (x,y) is given by:

    x_new = xx * x + xy * y + x0
    y_new = yx * x + yy * y + y0

    The current transformation matrix of a Context, represented as a Matrix, defines the transformation from user-space coordinates to device-space coordinates.

    Some standard Python operators can be used with matrices:

    To read the values from a Matrix:

    xx, yx, xy, yy, x0, y0 = matrix
    To multiply two matrices:

    matrix3 = matrix1.multiply(matrix2)
    # or equivalently
    matrix3 = matrix1 * matrix2
    To compare two matrices:

    matrix1 == matrix2
    matrix1 != matrix2
    For more information on matrix transformation see http://www.cairographics.org/matrix_transform
    """
    _cairo.cairo_matrix_init.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)
    def __init__(self, xx=1.0, yx=0.0, xy=0.0, yy=1.0, x0=0.0, y0=0.0):
        """
        @param xx (float): xx component of the affine transformation
        @param yx (float): yx component of the affine transformation
        @param xy (float): xy component of the affine transformation
        @param yy (float): yy component of the affine transformation
        @param x0 (float): X translation component of the affine transformation
        @param y0 (float): Y translation component of the affine transformation

        Create a new Matrix with the affine transformation given by xx, yx, xy, yy, x0, y0. The transformation is given by:

        x_new = xx * x + xy * y + x0
        y_new = yx * x + yy * y + y0
        To create a new identity matrix:

        matrix = cairo.Matrix()
        To create a matrix with a transformation which translates by tx and ty in the X and Y dimensions, respectively:

        matrix = cairo.Matrix(x0=tx, y0=ty)
        To create a matrix with a transformation that scales by sx and sy in the X and Y dimensions, respectively:

        matrix = cairo.Matrix(xx=sy, yy=sy)
        """
        self._matrix_t = ctypes.pointer(cairo_matrix_t())
        _cairo.cairo_matrix_init(self._matrix_t, xx, yx, xy, yy, x0, y0)

    @property
    def _as_parameter_(self):
        return self._matrix_t

    @classmethod
    def _from_address(cls, address):
        matrix = object.__new__(cls)
        matrix._matrix_t = ctypes.POINTER(cairo_matrix_t).from_address(address)
        return matrix

    def invert(self):
        """
        Changes Matrix to be the inverse of it’s original value. Not all transformation matrices have inverses; if the matrix collapses points together (it is degenerate), then it has no inverse and this function will fail.
        """
        _cairo.cairo_matrix_invert(self._matrix_t)

    def multiply(self, matrix2):
        """
        Multiplies the affine transformations in Matrix and matrix2 together. The effect of the resulting transformation is to first apply the transformation in Matrix to the coordinates and then apply the transformation in matrix2 to the coordinates.

        It is allowable for result to be identical to either Matrix or matrix2.

        NOTE: the sentence above is not correct. There is no result as parameter. This function will always return a new matrix in casper-cairo.

        NOTE 2016/1/14: Should I make it compatible to cairo or pycairo?
        """
        result = Matrix()
        _cairo.cairo_matrix_multiply(result, self, matrix2)
        return result

    def rotate(self, radians):
        """
        @param radians: angle of rotation, in radians. The direction of rotation is defined such that positive angles rotate in the direction from the positive X axis toward the positive Y axis. With the default axis orientation of cairo, positive angles rotate in a clockwise direction.

        Applies rotation by radians to the transformation in matrix . The effect of the new transformation is to first rotate the coordinates by radians , then apply the original transformation to the coordinates.
        """
        _cairo.cairo_matrix_rotate(self, ctypes.c_double(radians))

    _cairo.cairo_matrix_scale.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.c_double)
    def scale(self, sx, sy):
        """
        Applies scaling by sx , sy to the transformation in matrix . The effect of the new transformation is to first scale the coordinates by sx and sy , then apply the original transformation to the coordinates.
        """
        _cairo.cairo_matrix_scale(self, sx, sy)

    def transform_distance(self, dx, dy):
        """
        Transforms the distance vector (dx ,dy ) by matrix . This is similar to cairo_matrix_transform_point() except that the translation components of the transformation are ignored. The calculation of the returned vector is as follows:

        dx2 = dx1 * a + dy1 * c;
        dy2 = dx1 * b + dy1 * d;

        Affine transformations are position invariant, so the same vector always transforms to the same vector. If (x1 ,y1 ) transforms to (x2 ,y2 ) then (x1 +dx1 ,y1 +dy1 ) will transform to (x1 +dx2 ,y1 +dy2 ) for all values of x1 and x2.
        """
        dx, dy = ctypes.c_double(dx), ctypes.c_double(dy)
        _cairo.cairo_matrix_transform_distance(self, ctypes.byref(dx), ctypes.byref(dy))

        return tuple(dx.value, dy.value)

    def transform_point(self, x, y):
        """
        Transforms the point (x , y ) by matrix.
        """
        x, y = ctypes.c_double(x), ctypes.c_double(y)
        _cairo.cairo_matrix_transform_point(self, ctypes.byref(x), ctypes.byref(y))
        return tuple(x.value, y.value)

    def translate(self, tx, ty):
        """
        Applies a transformation by tx, ty to the transformation in Matrix. The effect of the new transformation is to first translate the coordinates by tx and ty, then apply the original transformation to the coordinates.
        """
        _cairo.cairo_matrix_translate(self, ctypes.c_double(tx), ctypes.c_double(ty))

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
        path._path_t = ctypes.pointer(cairo_path_t.from_address(address))
        return path

class Pattern:

    def __init__(self):
        self._pattern_t = None

    @property
    def _as_parameter_(self):
        return self._pattern_t

    @classmethod
    def _from_address(cls, address):
        pattern = object.__new__(_pattern_types[_cairo.cairo_pattern_get_type(address)])
        pattern._pattern_t = address
        return pattern

    def get_extend(self):
        return _cairo.cairo_pattern_get_extend(self)

    def get_matrix(self):
        matrix = Matrix()
        _cairo.cairo_pattern_get_matrix(self, matrix)
        return matrix

    def set_extend(self, extend):
        _cairo.cairo_pattern_set_extend(self, extend)

    def set_matrix(self, matrix):
        _cairo.cairo_pattern_set_matrix(self, matrix)

    # Conflict: I didn't see any type requirement for gettting and setting filter for patterns in original cairo C lib but getting and setting filter are restricted to SurfacePattern objects in pycairo.
    def get_filter(self):
        return _cairo.cairo_pattern_get_filter(self)

    def set_filter(self, filter):
        _cairo.cairo_pattern_set_filter(self, filter)

class SolidPattern(Pattern):

    _cairo.cairo_pattern_create_rgba.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)
    def __init__(self, red, green, blue, alpha=1.0):
        self._pattern_t = _cairo.cairo_pattern_create_rgba(red, green, blue, alpha)

    _cairo.cairo_pattern_get_rgba.argtypes = (ctypes.c_void_p, ) + tuple(ctypes.POINTER(ctypes.c_double) for i in range(4))
    def get_rgba(self):
        red, green, blue, alpha = (ctypes.c_double() for i in range(4))
        _cairo.cairo_pattern_get_rgba(self, *tuple(ctypes.byref(i) for i in (red, green, blue, alpha)))
        return tuple(i.value for i in (red, green, blue, alpha))

class SurfacePattern(Pattern):

    def __init__(self, surface):
        self._pattern_t = _cairo.cairo_pattern_create_for_surface(surface)

    def get_surface(self):
        surface = ctypes.pointer(ctypes.c_void_p())
        _cairo.cairo_pattern_get_surface(self, surface)
        return Surface._from_address(surface.contents.value)

class Gradient(Pattern):

    _cairo.cairo_pattern_add_color_stop_rgb.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)
    def add_color_stop_rgb(self, offset, red, green, blue):
        _cairo.cairo_pattern_add_color_stop_rgb(self, offset, red, green, blue)

    _cairo.cairo_pattern_add_color_stop_rgba.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)
    def add_color_stop_rgba(self, offset, red, green, blue, alpha):
        _cairo.cairo_pattern_add_color_stop_rgba(self, offset, red, green, blue, alpha)

class LinearGradient(Gradient):

    _cairo.cairo_pattern_create_linear.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, )
    def __init__(self, x0, y0, x1, y1):
        self._pattern_t = _cairo.cairo_pattern_create_linear(x0, y0, x1, y1)

    def get_linear_points(self):
        x0, y0, x1, y1 = tuple(ctypes.c_double() for i in range(4))
        _cairo.cairo_pattern_get_linear_points(self, *tuple(ctypes.byref(i) for i in (x0, y0, x1, y1)))
        return tuple(i.value for i in (x0, y0, x1, y1))

class RadialGradient(Gradient):

    _cairo.cairo_pattern_create_radial.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, )
    def __init__(self, cx0, cy0, radius0, cx1, cy1, radius1):
        self._pattern_t = _cairo.cairo_pattern_create_radial(cx0, cy0, radius0, cx1, cy1, radius1)

    def get_radial_circles(self):
        x0, y0, r0, x1, y1, r1 = tuple(ctypes.c_double() for i in range(6))
        _cairo.cairo_pattern_get_linear_points(self, *tuple(ctypes.byref(i) for i in (x0, y0, r0, x1, y1, r1)))
        return tuple(i.value for i in (x0, y0, r0, x1, y1, r1))

#############

class FontFace:
    """
    A cairo.FontFace specifies all aspects of a font other than the size or font matrix (a font matrix is used to distort a font by sheering it or scaling it unequally in the two directions). A FontFace can be set on a Context by using Context.set_font_face() the size and font matrix are set with Context.set_font_size() and Context.set_font_matrix().

    There are various types of FontFace, depending on the font backend they use.

    This class cannot be instantiated directly, it is returned by Context.get_font_face().
    """
    def __init__(self):
        self._font_face_t = None

    @property
    def _as_parameter_(self):
        return self._font_face_t

    @classmethod
    def _from_address(cls, address):
        font_face = object.__new__(cls)
        font_face._font_face_t = address
        return font_face

    def status(self):
        return _cairo.cairo_font_face_status(self._font_face_t)

    def get_type(self):
        return _cairo.cairo_font_face_get_type(self._font_face_t)

    def get_reference_count(self):
        return _cairo.cairo_font_face_get_reference_count(self._font_face_t)

    def set_user_data(self):
        pass

    def get_user_data(self):
        pass

class ScaledFont:
    """
    A ScaledFont is a font scaled to a particular size and device resolution. A ScaledFont is most useful for low-level font usage where a library or application wants to cache a reference to a scaled font to speed up the computation of metrics.

    There are various types of scaled fonts, depending on the font backend they use.
    """
    def __init__(self, font_face, font_matrix, ctm, font_options):
        self._scaled_font_t = _cairo.cairo_scaled_font_create(font_face, font_matrix, ctm, font_options)

    @property
    def _as_parameter_(self):
        return self._scaled_font_t

    @classmethod
    def _from_address(cls, address):
        scaled_font = object.__new__(cls)
        scaled_font._scaled_font_t = address
        return scaled_font

    def extents(self):
        """
        @return: (ascent, descent, height, max_x_advance, max_y_advance), a tuple of float values.
        """
        font_extents_t = cairo_font_extents_t()
        _cairo.cairo_scaled_font_extents(self._scaled_font_t, ctypes.byref(font_extents_t))
        return tuple(getattr(font_extents_t, i[0]) for i in font_extents_t._fields_)

    def get_ctm(self):
        ctm = Matrix()
        _cairo.cairo_scaled_font_get_ctm(self, ctm)
        return ctm

    def get_font_face(self):
        return FontFace._from_address(_cairo.cairo_scaled_font_get_font_face(self))

    def get_font_matrix(self):
        matrix = Matrix()
        _cairo.cairo_scaled_font_get_font_matrix(self, matrix)
        return matrix

    def get_font_options(self):
        font_options = FontOptions()
        _cairo.cairo_scaled_font_get_font_options(self, font_options)
        return font_options

    def text_extents(self, text):
        extents_t = cairo_text_extents_t()
        text = text.encode("utf-8")
        _cairo.cairo_scaled_font_text_extents(self._scaled_font_t, text, ctypes.byref(extents_t))
        return tuple(getattr(extents_t, i[0]) for i in extents_t._fields_)

class FontOptions:
    """
    An opaque structure holding all options that are used when rendering fonts.

    Individual features of a FontOptions can be set or accessed using functions named FontOptions.set_<feature_name> and FontOptions.get_<feature_name>, like FontOptions.set_antialias() and FontOptions.get_antialias().

    New features may be added to a FontOptions in the future. For this reason, FontOptions.copy(), FontOptions.equal(), FontOptions.merge(), and FontOptions.hash() should be used to copy, check for equality, merge, or compute a hash value of FontOptions objects.
    """
    def __init__(self):
        self._font_options_t = None

    @property
    def _as_parameter_(self):
        return self._font_options_t

    @classmethod
    def _from_address(cls, address):
        font_options = object.__new__(cls)
        font_options._font_options_t = address
        return font_options
    
    for i in ("antialias", "hint_metrics", "hint_style", "subpixel_order"):
        exec("get_%s = lambda self: _cairo.cairo_font_options_get_%s(self)" % (i, i))
        exec("set_%s = lambda self, %s: _cairo.cairo_font_options_set_%s(self, %s)" % (i, i, i, i))

    del i

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

        This function uses cairo_surface_get_type() to determine the type of the cairo_surface_t and then transform them into a corresponding Python Surface type
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

    def write_to_png(self, fobj):
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
        if isinstance(fobj, str): 
            return _cairo.cairo_surface_write_to_png(self._surface_t, bytes(fobj, "utf-8")) # in case fobj is a filename

        def doWrite(closure, data, length):
            try:
                fobj.write(ctypes.string_at(data, length))
                return STATUS_SUCCESS
            except:
                return STATUS_WRITE_ERROR;

        return _cairo.cairo_surface_write_to_png_stream(self._surface_t, cairo_write_func_t(doWrite), None)

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
        Note 2016/1/13: Now data can be any Python supporting writable buffer.
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
        """Tested five methods:

        - ctypes.c_char_p method

        bb = bytearray(40000)
        b = ctypes.c_char_p.from_buffer(bb)
        s = ImageSurface.create_for_data(b, FORMAT_ARGB32, 100, 100, 400)

        Result: Does not work. bb doesn't seem to change.

        - ctypes.c_char_p, byref method

        bb = bytearray(40000)
        b = ctypes.c_char_p.from_buffer(bb)
        s = ImageSurface.create_for_data(ctypes.byref(b), FORMAT_ARGB32, 100, 100, 400)

        Result: Works. bb changes. But segmentation fault when accessing b.

        - ctypes.c_char_Array_* method

        bb = bytearray(40000)
        b = (ctypes.c_char*len(bb)).from_buffer(bb)
        s = ImageSurface.create_for_data(b, FORMAT_ARGB32, 100, 100, 400)

        Result: Works. bb changes. bb, b and s.get_data() change synchronously. No problem found.

        - ctypes.c_char_Array_*, byref method

        bb = bytearray(40000)
        b = (ctypes.c_char*len(bb)).from_buffer(bb)
        s = ImageSurface.create_for_data(ctypes.byref(b), FORMAT_ARGB32, 100, 100, 400)

        Result: Works. bb, b and s.get_data() change synchronously. No problem found.

        - ctypes.c_char, byref method

        bb = bytearray(40000)
        b = ctypes.c_char.from_buffer(bb)
        s = ImageSurface.create_for_data(ctypes.byref(b), FORMAT_ARGB32, 100, 100, 400)

        Result: Works. bb and s.get_data() change synchronously(b is a c_char so it does not support indexing). No problem found.

        I prefer the ctypes.c_char_Array_* method being inserted here to let @param data be any Python writable buffer.
        """
        return surface

    @classmethod
    def create_from_png(cls, fobj):
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
        if isinstance(fobj, str):
            surface._surface_t = _cairo.cairo_image_surface_create_from_png(bytes(filename, "utf-8"))
        else:
            def doRead(closure, data, length):
                try:
                    (ctypes.c_char * length).from_address(data).raw = fobj.read(length)
                    return STATUS_SUCCESS
                except:
                    return STATUS_READ_ERROR
            surface._surface_t = _cairo.cairo_image_surface_create_from_png_stream(cairo_read_func_t(doRead), None)
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
        cairo.ImageSurface.get_data() in pycairo (yet not available, in docs, while available in the LATEST release, returning a memoryview object)
        cairo_image_surface_get_data() in cairo
        """
        ## Still thinking about how to return a memoryview object which is more pythonic, though c_char_Array_* itself supports nearly everything a memoryview has.
        ## Note 2016/1/13: memoryview doenst support format <c. Don't know what's wrong.
        return (ctypes.c_char*(self.get_width()*self.get_height())).from_address(_cairo.cairo_image_surface_get_data(self._surface_t))

    def get_format(self):
        return _cairo.cairo_image_surface_get_format(self._surface_t)

    def get_height(self):
        return _cairo.cairo_image_surface_get_height(self._surface_t)

    def get_stride(self):
        return _cairo.cairo_image_surface_get_stride(self._surface_t)

    def get_width(self):
        return _cairo.cairo_image_surface_get_width(self._surface_t)

class SVGSurface(Surface):

    _cairo.cairo_svg_surface_create.argtypes = (ctypes.c_char_p, ctypes.c_double, ctypes.c_double)
    def __init__(self, filename, width_in_points, height_in_points):
        self._surface_t = _cairo.cairo_svg_surface_create(filename, width_in_points, height_in_points)

class Context:
    """
    Context is the main object used when drawing with cairo. To draw with cairo, you create a Context, set the target surface, and drawing options for the Context, create shapes with functions like Context.move_to() and Context.line_to(), and then draw shapes with Context.stroke() or Context.fill().

    Contexts can be pushed to a stack via Context.save(). They may then safely be changed, without loosing the current state. Use Context.restore() to restore to the saved state.
    """

    def __init__(self, target):
        """
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
        @param path (Path object): to be appended
        Append the path onto the current path. The path may be either the return value from one of Context.copy_path() or Context.copy_path_flat() or it may be constructed manually (in C).

        Origin:
        cairo.Context.append_path() in pycairo
        cairo_append_path() in cairo
        """
        _cairo.cairo_append_path(path._path_t)

    _cairo.cairo_arc.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)
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
        _cairo.cairo_arc(xc, yc, radius, angle1, angle2)

    _cairo.cairo_arc_negative.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)
    def arc_negative(self, xc, yc, radius, angle1, angle2):
        """
        Adds a circular arc of the given radius to the current path. The arc is centered at (xc, yc), begins at angle1 and proceeds in the direction of decreasing angles to end at angle2. If angle2 is greater than angle1 it will be progressively decreased by 2*PI until it is less than angle1.

        See Context.arc() for more details. This function differs only in the direction of the arc between the two angles.

        Origin:
        cairo.Context.arc_negative() in pycairo
        cairo_arc_negative() in cairo
        """
        _cairo.cairo_arc(xc, yc, radius, angle1, angle2)

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
        _cairo.cairo_curve_to(self._cairo_t, *[ctypes.c_double.from_param(i) for i in (x1, y1, x2, y2, x3, y3)])
        
    def destroy(self):
        pass

    def device_to_user(self, x, y):
        """
        @param x (float): X value of coordinate
        @param y (float): Y value of coordinate
        @return: (float, float)
        Transform a coordinate from device space to user space by multiplying the given point by the inverse of the current transformation matrix (CTM).

        Origin:
        cairo.device_to_user() in pycairo
        cairo_device_to_user() in cairo
        """
        x, y = ctypes.c_double(), ctypes.c_double()
        _cairo.cairo_device_to_user(self._cairo_t, ctypes.byref(x), ctypes.byref(y))
        return x.value, y.value

    def device_to_user_distance(self, dx, dy):
        """
        @param dx (float): X component of a distance vector
        @param dy (float):Y component of a distance vector
        @return: (float, float)
        Transform a distance vector from device space to user space. This function is similar to Context.device_to_user() except that the translation components of the inverse CTM will be ignored when transforming (dx,dy).

        Origin:
        cairo.device_to_user_distance() in pycairo
        cairo_device_to_user_distance() in cairo
        """
        dx, dy = ctypes.c_double(), ctypes.c_double()
        _cairo.cairo_device_to_user(self._cairo_t, ctypes.byref(dx), ctypes.byref(dy))
        return dx.value, dy.value

    def fill(self):
        """
        A drawing operator that fills the current path according to the current FILL RULE, (each sub-path is implicitly closed before being filled). After fill(), the current path will be cleared from the Context. See Context.set_fill_rule() and Context.fill_preserve().
        """
        _cairo.cairo_fill(self._cairo_t)

    # benjaminish
    def fill_extents(self):
        """
        @return: tuple(x1, y1, x2, y2)
        Computes a bounding box in user coordinates covering the area that would be affected, (the “inked” area), by a Context.fill() operation given the current path and fill parameters. If the current path is empty, returns an empty rectangle (0,0,0,0). Surface dimensions and clipping are not taken into account.

        Contrast with Context.path_extents(), which is similar, but returns non-zero extents for some paths with no inked area, (such as a simple line segment).

        Note that fill_extents() must necessarily do more work to compute the precise inked areas in light of the fill rule, so Context.path_extents() may be more desirable for sake of performance if the non-inked path extents are desired.

        See Context.fill(), Context.set_fill_rule() and Context.fill_preserve().
        """
        x1, y1, x2, y2 = (ctypes.c_double() for i in range(4))
        _cairo.cairo_fill_extents(self._cairo_t, *(ctypes.byref(i) for i in (x1, y1, x2, y2)))
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
        return tuple(getattr(font_extents_t, i[0]) for i in font_extents_t._fields_)
        """address = ctypes.c_int(0)
        _cairo.cairo_font_extents(self._cairo_t, ctypes.byref(address))
        return struct.unpack("5d", ctypes.string_at(address, ctypes.sizeof(ctypes.c_double)*5))"""

    def get_antialias(self):
        """
        @return int: the current ANTIALIAS mode, as set by Context.set_antialias().

        Origin:
        cairo.Context.get_antialias() in pycairo
        cairo_get_antialias() in cairo
        """
        return _cairo.cairo_get_antialias(self._cairo_t)

    def get_current_point(self):
        """
        @return (x, y)
            x: X coordinate of the current point
            y: Y coordinate of the current point

        Gets the current point of the current path, which is conceptually the final point reached by the path so far.

        The current point is returned in the user-space coordinate system. If there is no defined current point or if Context is in an error status, x and y will both be set to 0.0. It is possible to check this in advance with Context.has_current_point().

        Most path construction functions alter the current point. See the following for details on how they affect the current point: Context.new_path(), Context.new_sub_path(), Context.append_path(), Context.close_path(), Context.move_to(), Context.line_to(), Context.curve_to(), Context.rel_move_to(), Context.rel_line_to(), Context.rel_curve_to(), Context.arc(), Context.arc_negative(), Context.rectangle(), Context.text_path(), Context.glyph_path(), Context.stroke_to_path().

        Some functions use and alter the current point but do not otherwise change current path: Context.show_text().

        Some functions unset the current path and as a result, current point: Context.fill(), Context.stroke().

        Origin:
        cairo.Context.get_current_point() in pycairo
        cairo_get_current_point() in cairo (NOTE: in Paths section)
        """
        x, y = ctypes.c_double(), ctypes.c_double()
        _cairo.cairo_get_current_point(self._cairo_t, ctypes.byref(x), ctypes.byref(y))
        return (x.value, y.value)

    def get_dash(self):
        """
        @return (dashes, offset)
            dashes: return value for the dash array
            offset: return value for the current dash offset

        Gets the current dash array.

        Origin:
        cairo.Context.get_dash() in pycairo
        cairo_get_dash() in cairo
        """
        dashes = (ctypes.c_double * _cairo.cairo_get_dash_count(self._cairo_t))()
        offset = ctypes.c_double()
        _cairo.cairo_get_dash(self._cairo_t, ctypes.byref(dashes), ctypes.byref(offset))
        return (tuple(dashes), offset.value)

    def get_dash_count(self):
        """
        @return int: the length of the dash array, or 0 if no dash array set.
        See also Context.set_dash() and Context.get_dash().

        Origin:
        cairo.Context.get_dash_count() in pycairo
        cairo_get_dash_count() in cairo
        """
        return _cairo.cairo_get_dash_count(self._cairo_t)

    def get_fill_rule(self):
        """
        @return int: the current FILL RULE, as set by Context.set_fill_rule().

        Origin:
        cairo.Context.get_fill_rule() in pycairo
        cairo_get_fill_rule() in cairo
        """
        return _cairo.cairo_get_fill_rule(self._cairo_t)

    def get_font_face(self):
        """
        @return: the current FontFace for the Context.
        """
        return FontFace._from_address(_cairo.cairo_get_font_face(self._cairo_t))

    def get_font_matrix(self):
        """
        @return: a Matrix object
        Stores the current font matrix into matrix. See cairo.Context.set_font_matrix().

        Origin:
        cairo.Context.get_font_matrix() in pycairo
        cairo_get_font_matrix() in cairo
        """
        matrix = Matrix()
        _cairo.cairo_get_font_matrix(self, matrix)
        return matrix

    def get_font_options(self):
        """
        """
        font_options = FontOptions()
        _cairo.cairo_get_font_options(self._cairo_t, font_options)
        return font_options

    def get_group_target(self):
        """
        @return: the target Surface.
        Gets the current destination Surface for the Context. This is either the original target surface as passed to Context or the target surface for the current group as started by the most recent call to Context.push_group() or Context.push_group_with_content().

        Origin:
        cairo.Context.get_group_target() in pycairo
        cairo_get_group_target() in cairo
        """
        return Surface._from_address(_cairo.cairo_get_group_target(self._cairo_t))

    def get_line_cap(self):
        """
        @return: the current LINE_CAP style, as set by Context.set_line_cap()

        Origin:
        cairo.Context.get_line_cap() in pycairo
        cairo_get_line_cap() in cairo
        """
        return _cairo.cairo_get_line_cap(self._cairo_t)

    def get_line_join(self):
        """
        @return: the current LINE_JOIN style, as set by Context.set_line_join()

        Origin:
        cairo.Context.get_line_join() in pycairo
        cairo_get_line_join() in cairo
        """
        return _cairo.cairo_get_line_join(self._cairo_t)

    _cairo.cairo_get_line_width.restype = ctypes.c_double
    def get_line_width(self):
        """
        @return: the current line width

        This function returns the current line width value exactly as set by Context.set_line_width(). Note that the value is unchanged even if the CTM has changed between the calls to Context.set_line_width() and get_line_width().

        Origin:
        cairo.Context.get_line_width() in pycairo
        cairo_get_line_width() in cairo
        """
        return _cairo.cairo_get_line_width(self._cairo_t)

    def get_matrix(self):
        """
        @return: the current transformation Matrix(CTM)
        """
        matrix = Matrix()
        _cairo.cairo_get_matrix(self, matrix)
        return matrix

    def get_miter_limit(self):
        """
        @return: the current miter limit, as set by Context.set_miter_limit().
        """
        return _cairo.cairo_get_miter_limit(self._cairo_t).value

    def get_operator(self):
        """
        @return: the current compositing OPERATOR for a Context.
        """
        return _cairo.cairo_get_operator(self._cairo_t)

    def get_scaled_font(self):
        """
        @return: the current ScaledFont for a Context.
        """
        return ScaledFont._from_address(_cairo.cairo_get_scaled_font(self._cairo_t))

    def get_source(self):
        """
        @return: the current source Pattern for a Context.
        """
        return Pattern._from_address(_cairo.cairo_get_source(self._cairo_t))

    def get_target(self):
        """
        @return: the target Surface for the Context.
        """
        return Surface._from_address(_cairo.cairo_get_target(self._cairo_t))

    _cairo.cairo_get_tolerance.restype = ctypes.c_double
    def get_tolerance(self):
        """
        @return: the current tolerance value, as set by Context.set_tolerance().
        """
        return _cairo.cairo_get_tolerance(self._cairo_t)

    def glyph_extents(self, glyphs, num_glyphs=-1):
        pass

    def has_current_point(self):
        """
        Returns whether a current point is defined on the current path. See cairo_get_current_point() for details on the current point.
        """
        return True if _cairo.cairo_has_current_point(self) else False

    _cairo.cairo_in_fill.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.c_double)
    def in_fill(self, x, y):
        return True if _cairo.cairo_in_fill(self._cairo_t, x, y) else False

    _cairo.cairo_in_fill.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.c_double)
    def in_stroke(self, x, y):
        return True if _cairo.cairo_in_stroke(self._cairo_t, x, y) else False

    _cairo.cairo_line_to.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.c_double)
    def line_to(self, x, y):
        """
        Adds a line to the path from the current point to position (x, y) in user-space coordinates. After this call the current point will be (x, y).

        If there is no current point before the call to line_to() this function will behave as ctx.move_to(x, y).
        """
        _cairo.cairo_line_to(self._cairo_t, x, y)

    def mask(self, pattern):
        """
        A drawing operator that paints the current source using the alpha channel of pattern as a mask. (Opaque areas of pattern are painted with the source, transparent areas are not painted.)
        """
        _cairo.cairo_mask(self._cairo_t, pattern._pattern_t)

    def mask_surface(self, surface, x=0.0, y=0.0):
        """
        A drawing operator that paints the current source using the alpha channel of surface as a mask. (Opaque areas of surface are painted with the source, transparent areas are not painted.)
        """
        _cairo.cairo_mask_surface(self._cairo_t, surface, ctypes.c_double.from_param(x), ctypes.c_double.from_param(y))

    # for performance concerns?
    _cairo.cairo_move_to.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.c_double)
    def move_to(self, x, y):
        """
        Begin a new sub-path. After this call the current point will be (x, y).
        """
        _cairo.cairo_move_to(self._cairo_t, x, y)

    def reference(self, cr):
        _cairo.cairo_reference(self._cairo_t)
        return self

    def new_path(self):
        """
        Clears the current path. After this call there will be no path and no current point.
        """
        _cairo.cairo_new_path(self._cairo_t)

    def new_sub_path(self):
        """
        Begin a new sub-path. Note that the existing path is not affected. After this call there will be no current point.

        In many cases, this call is not needed since new sub-paths are frequently started with Context.move_to().

        A call to new_sub_path() is particularly useful when beginning a new sub-path with one of the Context.arc() calls. This makes things easier as it is no longer necessary to manually compute the arc’s initial coordinates for a call to Context.move_to().
        """
        _cairo.cairo_new_sub_path(self._cairo_t)

    def paint(self):
        """
        A drawing operator that paints the current source everywhere within the current clip region.
        """
        _cairo.cairo_paint(self._cairo_t)

    def paint_with_alpha(self, alpha):
        """
        @param alpha (float): alpha value, between 0 (transparent) and 1 (opaque)
        A drawing operator that paints the current source everywhere within the current clip region using a mask of constant alpha value alpha. The effect is similar to Context.paint(), but the drawing is faded out using the alpha value.
        """
        _cairo.cairo_paint_with_alpha(self._cairo_t, ctypes.c_double.from_param(alpha))

    def path_extents(self):
        """
        @param x1 (float): left of the resulting extents
        @param y1 (float): top of the resulting extents
        @param x2 (float): right of the resulting extents
        @param y2 (float): bottom of the resulting extents
        Computes a bounding box in user-space coordinates covering the points on the current path. If the current path is empty, returns an empty rectangle (0, 0, 0, 0). Stroke parameters, fill rule, surface dimensions and clipping are not taken into account.

        Contrast with Context.fill_extents() and Context.stroke_extents() which return the extents of only the area that would be “inked” by the corresponding drawing operations.

        The result of path_extents() is defined as equivalent to the limit of Context.stroke_extents() with cairo.LINE_CAP_ROUND as the line width approaches 0.0, (but never reaching the empty-rectangle returned by Context.stroke_extents() for a line width of 0.0).

        Specifically, this means that zero-area sub-paths such as Context.move_to(); Context.line_to() segments, (even degenerate cases where the coordinates to both calls are identical), will be considered as contributing to the extents. However, a lone Context.move_to() will not contribute to the results of Context.path_extents().
        """
        x1, y1, x2, y2 = (ctypes.c_double() for i in range(4))
        _cairo.cairo_path_extents(self, *(ctypes.byref(i) for i in (x1, y1, x2, y2)))
        return tuple(i.value for i in (x1, y1, x2, y2))

    def pop_group(self):
        """
        Terminates the redirection begun by a call to Context.push_group() or Context.push_group_with_content() and returns a new pattern containing the results of all drawing operations performed to the group.

        The pop_group() function calls Context.restore(), (balancing a call to Context.save() by the Context.push_group() function), so that any changes to the graphics state will not be visible outside the group.
        """
        return SurfacePattern._from_address(_cairo.cairo_pop_group(self))

    def pop_group_to_source(self):
        """
        Terminates the redirection begun by a call to Context.push_group() or Context.push_group_with_content() and installs the resulting pattern as the source Pattern in the given Context.

        The behavior of this function is equivalent to the sequence of operations:

        group = cairo_pop_group()
        ctx.set_source(group)

        but is more convenient as their is no need for a variable to store the short-lived pointer to the pattern.

        The Context.pop_group() function calls Context.restore(), (balancing a call to Context.save() by the Context.push_group() function), so that any changes to the graphics state will not be visible outside the group.
        """
        _cairo.cairo_pop_group_to_source(self._cairo_t)

    def push_group(self):
        """
        Temporarily redirects drawing to an intermediate surface known as a group. The redirection lasts until the group is completed by a call to Context.pop_group() or Context.pop_group_to_source(). These calls provide the result of any drawing to the group as a pattern, (either as an explicit object, or set as the source pattern).

        This group functionality can be convenient for performing intermediate compositing. One common use of a group is to render objects as opaque within the group, (so that they occlude each other), and then blend the result with translucence onto the destination.

        Groups can be nested arbitrarily deep by making balanced calls to Context.push_group()/Context.pop_group(). Each call pushes/pops the new target group onto/from a stack.

        The push_group() function calls Context.save() so that any changes to the graphics state will not be visible outside the group, (the pop_group functions call Context.restore()).

        By default the intermediate group will have a CONTENT type of cairo.CONTENT_COLOR_ALPHA. Other content types can be chosen for the group by using Context.push_group_with_content() instead.

        As an example, here is how one might fill and stroke a path with translucence, but without any portion of the fill being visible under the stroke:

        ctx.push_group()
        ctx.set_source(fill_pattern)
        ctx.fill_preserve()
        ctx.set_source(stroke_pattern)
        ctx.stroke()
        ctx.pop_group_to_source()
        ctx.paint_with_alpha(alpha)
        """
        _cairo.cairo_push_group(self)

    def push_group_with_content(self, content):
        """
        @param content: a CONTENT indicating the type of group that will be created
        Temporarily redirects drawing to an intermediate surface known as a group. The redirection lasts until the group is completed by a call to Context.pop_group() or Context.pop_group_to_source(). These calls provide the result of any drawing to the group as a pattern, (either as an explicit object, or set as the source pattern).

        The group will have a content type of content. The ability to control this content type is the only distinction between this function and Context.push_group() which you should see for a more detailed description of group rendering.
        """
        _cairo.cairo_push_group_with_content(self, content)

    _cairo.cairo_rectangle.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)
    def rectangle(self, x, y, width, height):
        """
        @param x (float): the X coordinate of the top left corner of the rectangle
        @param y (float): the Y coordinate to the top left corner of the @paramrectangle
        @param width (float): the width of the rectangle
        @param height (float): the height of the rectangle

        Adds a closed sub-path rectangle of the given size to the current path at position (x, y) in user-space coordinates.

        This function is logically equivalent to:

        ctx.move_to(x, y)
        ctx.rel_line_to(width, 0)
        ctx.rel_line_to(0, height)
        ctx.rel_line_to(-width, 0)
        ctx.close_path()

        Origin:
        cairo.Context.rectangle() in pycairo
        cairo_rectangle in cairo
        """
        #x, y, width, height = tuple(ctypes.c_double(i) for i in (x, y, width, height))
        #_cairo.cairo_rectangle.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)
        _cairo.cairo_rectangle(self._cairo_t, x, y, width, height)

    _cairo.cairo_rel_curve_to.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, )
    def rel_curve_to(self, dx1, dy1, dx2, dy2, dx3, dy3):
        """
        Relative-coordinate version of Context.curve_to(). All offsets are relative to the current point. Adds a cubic Bézier spline to the path from the current point to a point offset from the current point by (dx3, dy3), using points offset by (dx1, dy1) and (dx2, dy2) as the control points. After this call the current point will be offset by (dx3, dy3).

        Given a current point of (x, y), ctx.rel_curve_to(dx1, dy1, dx2, dy2, dx3, dy3) is logically equivalent to ctx.curve_to(x+dx1, y+dy1, x+dx2, y+dy2, x+dx3, y+dy3).
        """
        _cairo.cairo_rel_curve_to(self, dx1, dy1, dx2, dy2, dx3, dy3)

    _cairo.cairo_rel_move_to.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.c_double)
    def rel_move_to(self, dx, dy):
        """
        Begin a new sub-path. After this call the current point will offset by (dx, dy).

        Given a current point of (x, y), ctx.rel_move_to(dx, dy) is logically equivalent to ctx.(x + dx, y + dy).
        """
        _cairo.cairo_rel_move_to(self, dx, dy)

    def reset_clip(self):
        """
        Reset the current clip region to its original, unrestricted state. That is, set the clip region to an infinitely large shape containing the target surface. Equivalently, if infinity is too hard to grasp, one can imagine the clip region being reset to the exact bounds of the target surface.

        Note that code meant to be reusable should not call reset_clip() as it will cause results unexpected by higher-level code which calls clip(). Consider using save() and restore() around clip() as a more robust means of temporarily restricting the clip region.
        """
        _cairo.cairo_reset_clip(self._cairo_t)

    def restore(self):
        """
        Restores Context to the state saved by a preceding call to save() and removes that state from the stack of saved states.
        """
        _cairo.cairo_restore(self._cairo_t)

    _cairo.cairo_rotate.argtypes = (ctypes.c_void_p, ctypes.c_double)
    def rotate(self, angle):
        """
        Modifies the current transformation matrix (CTM) by rotating the user-space axes by angle radians. The rotation of the axes takes places after any existing transformation of user space. The rotation direction for positive angles is from the positive X axis toward the positive Y axis.
        """
        _cairo.cairo_rotate(self, angle)

    def save(self):
        """
        Makes a copy of the current state of Context and saves it on an internal stack of saved states. When restore() is called, Context will be restored to the saved state. Multiple calls to save() and restore() can be nested; each call to restore() restores the state from the matching paired save().
        """
        _cairo.cairo_save(self._cairo_t)

    _cairo.cairo_scale.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.c_double)
    def scale(self, sx, sy):
        """
        Modifies the current transformation matrix (CTM) by scaling the X and Y user-space axes by sx and sy respectively. The scaling of the axes takes place after any existing transformation of user space.
        """
        _cairo.cairo_scale(self, sx, sy)

    _cairo.cairo_select_font_face.argtypes = (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_int)
    def select_font_face(self, family, slant=FONT_SLANT_NORMAL, weight=FONT_WEIGHT_NORMAL):
        """
        Note: The select_font_face() function call is part of what the cairo designers call the “toy” text API. It is convenient for short demos and simple programs, but it is not expected to be adequate for serious text-using applications.

        Selects a family and style of font from a simplified description as a family name, slant and weight. Cairo provides no operation to list available family names on the system (this is a “toy”, remember), but the standard CSS2 generic family names, (“serif”, “sans-serif”, “cursive”, “fantasy”, “monospace”), are likely to work as expected.

        For “real” font selection, see the font-backend-specific font_face_create functions for the font backend you are using. (For example, if you are using the freetype-based cairo-ft font backend, see cairo_ft_font_face_create_for_ft_face() or cairo_ft_font_face_create_for_pattern().) The resulting font face could then be used with cairo_scaled_font_create() and cairo_set_scaled_font().

        Similarly, when using the “real” font support, you can call directly into the underlying font system, (such as fontconfig or freetype), for operations such as listing available fonts, etc.

        It is expected that most applications will need to use a more comprehensive font handling and text layout library, (for example, pango), in conjunction with cairo.

        If text is drawn without a call to select_font_face(), (nor set_font_face() nor set_scaled_font()), the default family is platform-specific, but is essentially “sans-serif”. Default slant is cairo.FONT_SLANT_NORMAL, and default weight is cairo.FONT_WEIGHT_NORMAL.

        This function is equivalent to a call to ToyFontFace followed by set_font_face().
        """
        _cairo.cairo_select_font_face(self, bytes(family, "utf-8"), slant, weight)

    def set_antialias(self, antialis):
        """
        Set the antialiasing mode of the rasterizer used for drawing shapes. This value is a hint, and a particular backend may or may not support a particular value. At the current time, no backend supports cairo.ANTIALIAS_SUBPIXEL when drawing shapes.

        Note that this option does not affect text rendering, instead see FontOptions.set_antialias().
        """
        _cairo.cairo_set_antialias(self._cairo_t, antialis)

    def set_dash(self, dashes, offset=0):
        """
        Sets the dash pattern to be used by stroke(). A dash pattern is specified by dashes - a sequence of positive values. Each value provides the length of alternate “on” and “off” portions of the stroke. The offset specifies an offset into the pattern at which the stroke begins.

        Each “on” segment will have caps applied as if the segment were a separate sub-path. In particular, it is valid to use an “on” length of 0.0 with cairo.LINE_CAP_ROUND or cairo.LINE_CAP_SQUARE in order to distributed dots or squares along a path.

        Note: The length values are in user-space units as evaluated at the time of stroking. This is not necessarily the same as the user space at the time of set_dash().

        If the number of dashes is 0 dashing is disabled.

        If the number of dashes is 1 a symmetric pattern is assumed with alternating on and off portions of the size specified by the single value in dashes.

        NOTE: pycairo has requires a wrong type for 'offset' which should have been a double in cairo.
        """
        _cairo.cairo_set_dash(self, (ctypes.c_double*len(dashes))(*dashes), len(dashes), ctypes.c_double.from_param(offset))

    def set_fill_rule(self, fill_rule):
        """
        @param fill_rule (int): a FILL RULE to set the within the cairo context. The fill rule is used to determine which regions are inside or outside a complex (potentially self-intersecting) path. The current fill rule affects both fill() and clip().

        The default fill rule is cairo.FILL_RULE_WINDING.
        """
        _cairo.cairo_set_fill_rule(self._cairo_t, fill_rule)

    def set_font_face(self, font_face):
        """
        @param font_face: a FontFace, or None to restore to the default FontFace
        Replaces the current FontFace object in the Context with font_face.
        """
        _cairo.cairo_set_font_face(self._cairo_t, font_face)

    def set_font_matrix(self, matrix):
        """
        @param matrix: a Matrix describing a transform to be applied to the current font.
        Sets the current font matrix to matrix. The font matrix gives a transformation from the design space of the font (in this space, the em-square is 1 unit by 1 unit) to user space. Normally, a simple scale is used (see set_font_size()), but a more complex font matrix can be used to shear the font or stretch it unequally along the two axes
        """
        _cairo.cairo_set_font_matrix(self, matrix)

    def set_font_options(self, options):
        """
        @param options: FontOptions to use
        Sets a set of custom font rendering options for the Context. Rendering options are derived by merging these options with the options derived from underlying surface; if the value in options has a default value (like cairo.ANTIALIAS_DEFAULT), then the value from the surface is used.
        """
        _cairo.cairo_set_font_options(self, options)

    def set_font_size(self, size):
        """
        @param size (float): the new font size, in user space units
        Sets the current font matrix to a scale by a factor of size, replacing any font matrix previously set with set_font_size() or set_font_matrix(). This results in a font size of size user space units. (More precisely, this matrix will result in the font’s em-square being a size by size square in user space.)

        If text is drawn without a call to set_font_size(), (nor set_font_matrix() nor set_scaled_font()), the default font size is 10.0.
        """
        _cairo.cairo_set_font_size(self, ctypes.c_double.from_param(size))

    def set_line_cap(self, line_cap):
        """
        @param line_cap: a LINE_CAP style
        Sets the current line cap style within the Context.

        As with the other stroke parameters, the current line cap style is examined by stroke(), stroke_extents(), and stroke_to_path(), but does not have any effect during path construction.

        The default line cap style is cairo.LINE_CAP_BUTT.
        """
        _cairo.cairo_set_line_cap(self, line_cap)

    def set_line_join(self, line_join):
        """
        @param line_join: a LINE_JOIN style
        Sets the current line join style within the Context.

        As with the other stroke parameters, the current line join style is examined by stroke(), stroke_extents(), and stroke_to_path(), but does not have any effect during path construction.

        The default line join style is cairo.LINE_JOIN_MITER.
        """
        _cairo.cairo_set_line_join(self, line_join)

    def set_line_width(self, width):
        """
        @param width (float): a line width
        Sets the current line width within the Context. The line width value specifies the diameter of a pen that is circular in user space, (though device-space pen may be an ellipse in general due to scaling/shear/rotation of the CTM).

        Note: When the description above refers to user space and CTM it refers to the user space and CTM in effect at the time of the stroking operation, not the user space and CTM in effect at the time of the call to set_line_width(). The simplest usage makes both of these spaces identical. That is, if there is no change to the CTM between a call to set_line_width() and the stroking operation, then one can just pass user-space values to set_line_width() and ignore this note.

        As with the other stroke parameters, the current line width is examined by stroke(), stroke_extents(), and stroke_to_path(), but does not have any effect during path construction.
        """
        _cairo.cairo_set_line_width(self, ctypes.c_double.from_param(width))

    def set_matrix(self, matrix):
        """
        @param matrix: a transformation Matrix from user space to device space.
        Modifies the current transformation matrix (CTM) by setting it equal to matrix.
        """
        _cairo.cairo_set_matrix(self, matrix)

    def set_miter_limit(self, limit):
        """
        Sets the current miter limit within the Context.

        If the current line join style is set to cairo.LINE_JOIN_MITER (see set_line_join()), the miter limit is used to determine whether the lines should be joined with a bevel instead of a miter. Cairo divides the length of the miter by the line width. If the result is greater than the miter limit, the style is converted to a bevel.

        As with the other stroke parameters, the current line miter limit is examined by stroke(), stroke_extents(), and stroke_to_path(), but does not have any effect during path construction.

        The default miter limit value is 10.0, which will convert joins with interior angles less than 11 degrees to bevels instead of miters. For reference, a miter limit of 2.0 makes the miter cutoff at 60 degrees, and a miter limit of 1.414 makes the cutoff at 90 degrees.

        A miter limit for a desired angle can be computed as:

        miter limit = 1/math.sin(angle/2)
        """
        _cairo.cairo_set_miter_limit(self, ctypes.c_double.from_param(limit))

    def set_operator(self, op):
        """
        @param op: the compositing OPERATOR to set for use in all drawing operations.
        The default operator is cairo.OPERATOR_OVER.
        """
        _cairo.cairo_set_operator(self, op)

    def set_scaled_font(self, scaled_font):
        """
        @param scaled_font: a ScaledFont
        Replaces the current font face, font matrix, and font options in the Context with those of the ScaledFont. Except for some translation, the current CTM of the Context should be the same as that of the ScaledFont, which can be accessed using ScaledFont.get_ctm().
        """
        _cairo.cairo_set_scaled_font(self, scaled_font)

    def set_source(self, source):
        """
        @param source: a Pattern to be used as the source for subsequent drawing operations.
        Sets the source pattern within Context to source. This pattern will then be used for any subsequent drawing operation until a new source pattern is set.

        Note: The pattern’s transformation matrix will be locked to the user space in effect at the time of set_source(). This means that further modifications of the current transformation matrix will not affect the source pattern. See Pattern.set_matrix().

        The default source pattern is a solid pattern that is opaque black, (that is, it is equivalent to set_source_rgb(0.0, 0.0, 0.0).
        """
        _cairo.cairo_set_source(self._cairo_t, source._pattern_t)

    _cairo.cairo_set_source_rgb.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double)
    def set_source_rgb(self, red, green, blue):
        """
        @param red (float): red component of color
        @param green (float): green component of color
        @param blue (float): blue component of color
        Sets the source pattern within Context to an opaque color. This opaque color will then be used for any subsequent drawing operation until a new source pattern is set.

        The color components are floating point numbers in the range 0 to 1. If the values passed in are outside that range, they will be clamped.

        The default source pattern is opaque black, (that is, it is equivalent to set_source_rgb(0.0, 0.0, 0.0).
        """
        _cairo.cairo_set_source_rgb(self._cairo_t, red, green, blue)

    _cairo.cairo_set_source_rgba.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)
    def set_source_rgba(self, red, green, blue, alpha=1.0):
        """
        @param red (float): red component of color
        @param green (float): green component of color
        @param blue (float): blue component of color
        @param alpha (float): alpha component of color
        Sets the source pattern within Context to a translucent color. This color will then be used for any subsequent drawing operation until a new source pattern is set.

        The color and alpha components are floating point numbers in the range 0 to 1. If the values passed in are outside that range, they will be clamped.

        The default source pattern is opaque black, (that is, it is equivalent to set_source_rgba(0.0, 0.0, 0.0, 1.0).
        """
        _cairo.cairo_set_source_rgba(self._cairo_t, red, green, blue, alpha)

    _cairo.cairo_set_source_surface.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double, ctypes.c_double)
    def set_source_surface(self, surface, x=0.0, y=0.0):
        """
        @param surface: a Surface to be used to set the source pattern
        @param x (float): User-space X coordinate for surface origin
        @param y (float): User-space Y coordinate for surface origin
        This is a convenience function for creating a pattern from a Surface and setting it as the source in Context with set_source().

        The x and y parameters give the user-space coordinate at which the surface origin should appear. (The surface origin is its upper-left corner before any transformation has been applied.) The x and y patterns are negated and then set as translation values in the pattern matrix.

        Other than the initial translation pattern matrix, as described above, all other pattern attributes, (such as its extend mode), are set to the default values as in SurfacePattern. The resulting pattern can be queried with get_source() so that these attributes can be modified if desired, (eg. to create a repeating pattern with Pattern.set_extend()).
        """
        _cairo.cairo_set_source_surface(self._cairo_t, surface._surface_t, x, y)

    _cairo.cairo_set_tolerance.argtypes = (ctypes.c_void_p, ctypes.c_double)
    def set_tolerance(self, tolerance):
        """
        tolerance (float) – the tolerance, in device units (typically pixels)
        Sets the tolerance used when converting paths into trapezoids. Curved segments of the path will be subdivided until the maximum deviation between the original path and the polygonal approximation is less than tolerance. The default value is 0.1. A larger value will give better performance, a smaller value, better appearance. (Reducing the value from the default value of 0.1 is unlikely to improve appearance significantly.) The accuracy of paths within Cairo is limited by the precision of its internal arithmetic, and the prescribed tolerance is restricted to the smallest representable internal value.
        """
        _cairo.cairo_set_tolerance(self, tolerance)

    def show_glyphs(self, glyphs, num_glyphs=-1):
        """
        @param glyphs (a sequence of (int, float, float)): glyphs to show
        @param num_glyphs (int): number of glyphs to show, defaults to showing all glyphs
        A drawing operator that generates the shape from an array of glyphs, rendered according to the current font face, font size (font matrix), and font options.
        """
        if num_glyphs < 0: num_glyphs = len(glyphs)
        array = (cairo_glyph_t * num_glyphs)(*glyphs[:num_glyphs])
        # something just feels no sense here.
        _cairo.show_glyphs(self, array, num_glyphs)

    def show_page(self):
        """
        Emits and clears the current page for backends that support multiple pages. Use copy_page() if you don’t want to clear the page.

        This is a convenience function that simply calls ctx.get_target() . show_page()
        """
        _cairo.cairo_show_page(self)

    _cairo.cairo_show_text.argtypes = (ctypes.c_void_p, ctypes.c_char_p)
    def show_text(self, utf8):
        """
        A drawing operator that generates the shape from a string of text, rendered according to the current font_face, font_size (font_matrix), and font_options.

        This function first computes a set of glyphs for the string of text. The first glyph is placed so that its origin is at the current point. The origin of each subsequent glyph is offset from that of the previous glyph by the advance values of the previous glyph.

        After this call the current point is moved to the origin of where the next glyph would be placed in this same progression. That is, the current point will be at the origin of the final glyph offset by its advance values. This allows for easy display of a single logical string with multiple calls to show_text().

        Note: The show_text() function call is part of what the cairo designers call the “toy” text API. It is convenient for short demos and simple programs, but it is not expected to be adequate for serious text-using applications. See show_glyphs() for the “real” text display API in cairo.
        """
        _cairo.cairo_show_text(self, bytes(utf8, "utf-8"))

    def stroke(self):
        """
        A drawing operator that strokes the current path according to the current line width, line join, line cap, and dash settings. After stroke(), the current path will be cleared from the cairo context. See set_line_width(), set_line_join(), set_line_cap(), set_dash(), and stroke_preserve().

        Note: Degenerate segments and sub-paths are treated specially and provide a useful result. These can result in two different situations:

        1. Zero-length “on” segments set in set_dash(). If the cap style is cairo.LINE_CAP_ROUND or cairo.LINE_CAP_SQUARE then these segments will be drawn as circular dots or squares respectively. In the case of cairo.LINE_CAP_SQUARE, the orientation of the squares is determined by the direction of the underlying path.

        2. A sub-path created by move_to() followed by either a close_path() or one or more calls to line_to() to the same coordinate as the move_to(). If the cap style is cairo.LINE_CAP_ROUND then these sub-paths will be drawn as circular dots. Note that in the case of cairo.LINE_CAP_SQUARE a degenerate sub-path will not be drawn at all, (since the correct orientation is indeterminate).

        In no case will a cap style of cairo.LINE_CAP_BUTT cause anything to be drawn in the case of either degenerate segments or sub-paths.
        """
        _cairo.cairo_stroke(self)

    def stroke_extents(self):
        """
        @returns (x1: float, y1: float, x2: float, y2: float)
        x1: left of the resulting extents
        y1: top of the resulting extents
        x2: right of the resulting extents
        y2: bottom of the resulting extents
        Computes a bounding box in user coordinates covering the area that would be affected, (the “inked” area), by a stroke() operation given the current path and stroke parameters. If the current path is empty, returns an empty rectangle (0, 0, 0, 0). Surface dimensions and clipping are not taken into account.

        Note that if the line width is set to exactly zero, then stroke_extents() will return an empty rectangle. Contrast with path_extents() which can be used to compute the non-empty bounds as the line width approaches zero.

        Note that stroke_extents() must necessarily do more work to compute the precise inked areas in light of the stroke parameters, so path_extents() may be more desirable for sake of performance if non-inked path extents are desired.

        See stroke(), set_line_width(), set_line_join(), set_line_cap(), set_dash(), and stroke_preserve().
        """
        x1, y1, x2, y2 = (ctypes.c_double() for i in range(4))
        _cairo.cairo_stroke_extents(self, *(ctypes.byref(i) for i in (x1, y1, x2, y2)))
        return (i.value for i in (x1, y1, x2, y2))

    def stroke_preserve(self):
        """
        A drawing operator that strokes the current path according to the current line width, line join, line cap, and dash settings. Unlike stroke(), stroke_preserve() preserves the path within the cairo context.

        See set_line_width(), set_line_join(), set_line_cap(), set_dash(), and stroke_preserve().
        """
        _cairo.cairo_stroke_preserve(self)

    def text_extents(self, utf8):
        """
        @param utf8 (bytes containing characters encoded utf-8): text to get extents for
        @returns: (x_bearing, y_bearing, width, height, x_advance, y_advance)
        Gets the extents for a string of text. The extents describe a user-space rectangle that encloses the “inked” portion of the text, (as it would be drawn by Context.show_text()). Additionally, the x_advance and y_advance values indicate the amount by which the current point would be advanced by Context.show_text().

        Note that whitespace characters do not directly contribute to the size of the rectangle (extents.width and extents.height). They do contribute indirectly by changing the position of non-whitespace characters. In particular, trailing whitespace characters are likely to not affect the size of the rectangle, though they will affect the x_advance and y_advance values.
        """
        extents = cairo_text_extents_t()
        _cairo.cairo_text_extents(self, bytes(utf8, "utf-8"), ctypes.byref(extents))
        return tuple(getattr(extents, i[0]) for i in extents._fields_)

    _cairo.cairo_text_path.argtypes = (ctypes.c_void_p, ctypes.c_char_p)
    def text_path(self, utf8):
        """
        Adds closed paths for text to the current path. The generated path if filled, achieves an effect similar to that of Context.show_text().

        Text conversion and positioning is done similar to Context.show_text().

        Like Context.show_text(), After this call the current point is moved to the origin of where the next glyph would be placed in this same progression. That is, the current point will be at the origin of the final glyph offset by its advance values. This allows for chaining multiple calls to to Context.text_path() without having to set current point in between.

        Note: The text_path() function call is part of what the cairo designers call the “toy” text API. It is convenient for short demos and simple programs, but it is not expected to be adequate for serious text-using applications. See Context.glyph_path() for the “real” text path API in cairo.
        """
        _cairo.cairo_text_path(self._cairo_t, bytes(utf8, "utf-8"))

    def transform(self, matrix):
        """
        @param matrix: a transformation Matrix to be applied to the user-space axes
        Modifies the current transformation matrix (CTM) by applying matrix as an additional transformation. The new transformation of user space takes place after any existing transformation.
        """
        _cairo.cairo_transform(self, matrix)

    _cairo.cairo_translate.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.c_double)
    def translate(self, tx, ty):
        """
        @param tx (float): amount to translate in the X direction
        @param ty (float): amount to translate in the Y direction
        Modifies the current transformation matrix (CTM) by translating the user-space origin by (tx, ty). This offset is interpreted as a user-space coordinate according to the CTM in place before the new call to translate(). In other words, the translation of the user-space origin takes place after any existing transformation.
        """
        _cairo.cairo_translate(self, tx, ty)

    def user_to_device(self, x, y):
        """
        @param x (float): X value of coordinate
        @param y (float): Y value of coordinate
        @return: (float, float)
        Transform a coordinate from user space to device space by multiplying the given point by the current transformation matrix (CTM).

        Origin:
        cairo.device_to_user() in pycairo
        cairo_device_to_user() in cairo
        """
        x, y = ctypes.c_double(), ctypes.c_double()
        _cairo.cairo_user_to_device(self._cairo_t, ctypes.byref(x), ctypes.byref(y))
        return x.value, y.value

    def user_to_device_distance(self, dx, dy):
        """
        @param dx (float): X component of a distance vector
        @param dy (float):Y component of a distance vector
        @return: (float, float)
        Transform a distance vector from user space to device space. This function is similar to Context.user_to_device() except that the translation components of the CTM will be ignored when transforming (dx,dy).

        Origin:
        cairo.user_to_device_distance() in pycairo
        cairo_user_to_device_distance() in cairo
        """
        dx, dy = ctypes.c_double(), ctypes.c_double()
        _cairo.cairo_user_to_device(self._cairo_t, ctypes.byref(dx), ctypes.byref(dy))
        return dx.value, dy.value

    def status(self):
        return _cairo.cairo_status(self._cairo_t)

    def save(self):
        _cairo.cairo_save(self._cairo_t)

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

_pattern_types = {
    PATTERN_TYPE_SOLID: SolidPattern,
    PATTERN_TYPE_SURFACE: SurfacePattern,
    PATTERN_TYPE_LINEAR: LinearGradient,
    PATTERN_TYPE_RADIAL: RadialGradient,
    PATTERN_TYPE_MESH: None,
    PATTERN_TYPE_RASTER_SOURC: None,
}

def version():
    return _cairo.cairo_version()

_cairo.cairo_version_string.restype = ctypes.c_char_p
def version_string():
    return str(_cairo.cairo_version_string(), "utf-8")

if __name__ == "__main__":
    # testing
    import array
    bb = bytearray(400 * 400 * 4)
    #bb = array.array("I", range(400*400))
    #b = (ctypes.c_char*len(bb)).from_buffer(bb)
    b = ctypes.POINTER(ctypes.c_uint)(ctypes.c_char_p.from_buffer(bb))
    #b = ctypes.cast(b, ctypes.POINTER(ctypes.c_int))
    s = ImageSurface.create_for_data(b, FORMAT_RGB24, 400, 400, 1600)
    c = Context(s)
    linear = LinearGradient(0, 0, 400, 400)
    linear.add_color_stop_rgb(0, 0, 0.3, 0.8)
    linear.add_color_stop_rgb(1, 0, 0.8, 0.3)
    c.set_source(linear)
    c.paint()

    radial = RadialGradient(200, 200, 25, 200, 200, 75)
    #radial.add_color_stop_rgba(0, 0, 0, 0, 1)
    #radial.add_color_stop_rgba(0.5, 0, 0, 0, 0)
    radial.add_color_stop_rgb(0, 1, 1, 1)
    radial.add_color_stop_rgb(1, 0.7, 0.7, 0.7)

    c.set_source(linear)
    c.mask(radial)
    c.set_font_size(50)
    c.move_to(0, 400)
    c.set_source_rgb(1, 1, 1)
    c.show_text("hello")
    
    with open("hello.png", "wb+") as f:
        s.write_to_png(f)

    #s = SVGSurface(b"output.svg", 1000, 1000)
    #c = Context(s)
    #c.move_to(0, 0)
    #c.line_to(1000, 1000)
    #c.stroke()
