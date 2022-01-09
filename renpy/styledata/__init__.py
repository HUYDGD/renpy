# Copyright 2004-2022 Tom Rothamel <pytom@bishoujo.us>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


from __future__ import print_function

import renpy
renpy.update_path()

def import_style_functions():
    import renpy.styledata.stylesets  # @UnresolvedImport

    import renpy.styledata.style_functions  # @UnresolvedImport
    import renpy.styledata.style_activate_functions  # @UnresolvedImport
    import renpy.styledata.style_hover_functions  # @UnresolvedImport
    import renpy.styledata.style_idle_functions  # @UnresolvedImport
    import renpy.styledata.style_insensitive_functions  # @UnresolvedImport

    import renpy.styledata.style_selected_functions  # @UnresolvedImport
    import renpy.styledata.style_selected_activate_functions  # @UnresolvedImport
    import renpy.styledata.style_selected_hover_functions  # @UnresolvedImport
    import renpy.styledata.style_selected_idle_functions  # @UnresolvedImport
    import renpy.styledata.style_selected_insensitive_functions  # @UnresolvedImport

    import renpy.styledata.styleclass  # @UnresolvedImport
    renpy.style.Style = renpy.styledata.styleclass.Style  # type: ignore

# Generated by scripts/relative_imports.py, do not edit below this line.
if 1 == 0:
    from . import style_activate_functions; style_activate_functions
    from . import style_functions; style_functions
    from . import style_hover_functions; style_hover_functions
    from . import style_idle_functions; style_idle_functions
    from . import style_insensitive_functions; style_insensitive_functions
    from . import style_selected_activate_functions; style_selected_activate_functions
    from . import style_selected_functions; style_selected_functions
    from . import style_selected_hover_functions; style_selected_hover_functions
    from . import style_selected_idle_functions; style_selected_idle_functions
    from . import style_selected_insensitive_functions; style_selected_insensitive_functions
    from . import styleclass; styleclass
    from . import stylesets; stylesets
    from . import styleutil; styleutil
