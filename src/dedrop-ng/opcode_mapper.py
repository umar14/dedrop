#!/usr/bin/python3

"""
$ ./python
Python 3.5.4 (default, Dec  9 2018, 19:40:53)
[GCC 7.3.0] on linux
>>> import dis; print(dis.opmap)
"""
# original_map = {'BUILD_MAP': 105, 'INPLACE_SUBTRACT': 56, 'BREAK_LOOP': 80, 'BEFORE_ASYNC_WITH': 52, 'DUP_TOP': 4, 'INPLACE_XOR': 78, 'SETUP_ASYNC_WITH': 154, 'SETUP_LOOP': 120, 'BUILD_SET': 104, 'BINARY_MATRIX_MULTIPLY': 16, 'INPLACE_ADD': 55, 'CALL_FUNCTION_KW': 141, 'LOAD_CLASSDEREF': 148, 'INPLACE_TRUE_DIVIDE': 29, 'UNPACK_SEQUENCE': 92, 'POP_JUMP_IF_FALSE': 114, 'CALL_FUNCTION': 131, 'ROT_TWO': 2, 'INPLACE_RSHIFT': 76, 'YIELD_FROM': 72, 'SETUP_EXCEPT': 121, 'SETUP_WITH': 143, 'BINARY_ADD': 23, 'GET_AWAITABLE': 73, 'SET_ADD': 146, 'LOAD_CONST': 100, 'BUILD_TUPLE_UNPACK': 152, 'GET_AITER': 50, 'LIST_APPEND': 145, 'STORE_DEREF': 137, 'COMPARE_OP': 107, 'INPLACE_POWER': 67, 'END_FINALLY': 88, 'DELETE_FAST': 126, 'JUMP_IF_TRUE_OR_POP': 112, 'BINARY_TRUE_DIVIDE': 27, 'DELETE_DEREF': 138, 'LOAD_GLOBAL': 116, 'ROT_THREE': 3, 'EXTENDED_ARG': 144, 'JUMP_ABSOLUTE': 113, 'BINARY_SUBTRACT': 24, 'CALL_FUNCTION_VAR_KW': 142, 'LOAD_ATTR': 106, 'DELETE_SUBSCR': 61, 'LOAD_BUILD_CLASS': 71, 'WITH_CLEANUP_FINISH': 82, 'CALL_FUNCTION_VAR': 140, 'GET_ANEXT': 51, 'BINARY_MULTIPLY': 20, 'UNARY_POSITIVE': 10, 'INPLACE_LSHIFT': 75, 'BUILD_MAP_UNPACK_WITH_CALL': 151, 'DELETE_GLOBAL': 98, 'POP_EXCEPT': 89, 'GET_ITER': 68, 'BUILD_SET_UNPACK': 153, 'BUILD_MAP_UNPACK': 150, 'DELETE_ATTR': 96, 'BINARY_AND': 64, 'STORE_GLOBAL': 97, 'IMPORT_STAR': 84, 'LOAD_DEREF': 136, 'DUP_TOP_TWO': 5, 'BUILD_LIST': 103, 'IMPORT_NAME': 108, 'YIELD_VALUE': 86, 'STORE_NAME': 90, 'UNARY_NEGATIVE': 11, 'UNARY_NOT': 12, 'BINARY_LSHIFT': 62, 'BUILD_TUPLE': 102, 'INPLACE_FLOOR_DIVIDE': 28, 'NOP': 9, 'RETURN_VALUE': 83, 'POP_BLOCK': 87, 'POP_TOP': 1, 'STORE_FAST': 125, 'POP_JUMP_IF_TRUE': 115, 'BINARY_MODULO': 22, 'BUILD_SLICE': 133, 'RAISE_VARARGS': 130, 'BINARY_FLOOR_DIVIDE': 26, 'GET_YIELD_FROM_ITER': 69, 'LOAD_FAST': 124, 'SETUP_FINALLY': 122, 'BINARY_OR': 66, 'CONTINUE_LOOP': 119, 'FOR_ITER': 93, 'LOAD_NAME': 101, 'UNARY_INVERT': 15, 'INPLACE_MATRIX_MULTIPLY': 17, 'INPLACE_MODULO': 59, 'JUMP_FORWARD': 110, 'MAP_ADD': 147, 'DELETE_NAME': 91, 'BINARY_XOR': 65, 'MAKE_FUNCTION': 132, 'BUILD_LIST_UNPACK': 149, 'LOAD_CLOSURE': 135, 'BINARY_SUBSCR': 25, 'PRINT_EXPR': 70, 'BINARY_POWER': 19, 'INPLACE_MULTIPLY': 57, 'IMPORT_FROM': 109, 'UNPACK_EX': 94, 'MAKE_CLOSURE': 134, 'STORE_SUBSCR': 60, 'INPLACE_OR': 79, 'STORE_ATTR': 95, 'INPLACE_AND': 77, 'JUMP_IF_FALSE_OR_POP': 111, 'WITH_CLEANUP_START': 81, 'BINARY_RSHIFT': 63}


"""
$ python
Python 3.7.2 (default, Mar 13 2019, 19:59:41)
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import dis; print(dis.opmap)
"""
original_map = {'POP_TOP': 1, 'ROT_TWO': 2, 'ROT_THREE': 3, 'DUP_TOP': 4, 'DUP_TOP_TWO': 5, 'NOP': 9, 'UNARY_POSITIVE': 10, 'UNARY_NEGATIVE': 11, 'UNARY_NOT': 12, 'UNARY_INVERT': 15, 'BINARY_MATRIX_MULTIPLY': 16, 'INPLACE_MATRIX_MULTIPLY': 17, 'BINARY_POWER': 19, 'BINARY_MULTIPLY': 20, 'BINARY_MODULO': 22, 'BINARY_ADD': 23, 'BINARY_SUBTRACT': 24, 'BINARY_SUBSCR': 25, 'BINARY_FLOOR_DIVIDE': 26, 'BINARY_TRUE_DIVIDE': 27, 'INPLACE_FLOOR_DIVIDE': 28, 'INPLACE_TRUE_DIVIDE': 29, 'GET_AITER': 50, 'GET_ANEXT': 51, 'BEFORE_ASYNC_WITH': 52, 'INPLACE_ADD': 55, 'INPLACE_SUBTRACT': 56, 'INPLACE_MULTIPLY': 57, 'INPLACE_MODULO': 59, 'STORE_SUBSCR': 60, 'DELETE_SUBSCR': 61, 'BINARY_LSHIFT': 62, 'BINARY_RSHIFT': 63, 'BINARY_AND': 64, 'BINARY_XOR': 65, 'BINARY_OR': 66, 'INPLACE_POWER': 67, 'GET_ITER': 68, 'GET_YIELD_FROM_ITER': 69, 'PRINT_EXPR': 70, 'LOAD_BUILD_CLASS': 71, 'YIELD_FROM': 72, 'GET_AWAITABLE': 73, 'INPLACE_LSHIFT': 75, 'INPLACE_RSHIFT': 76, 'INPLACE_AND': 77, 'INPLACE_XOR': 78, 'INPLACE_OR': 79, 'BREAK_LOOP': 80, 'WITH_CLEANUP_START': 81, 'WITH_CLEANUP_FINISH': 82, 'RETURN_VALUE': 83, 'IMPORT_STAR': 84, 'SETUP_ANNOTATIONS': 85, 'YIELD_VALUE': 86, 'POP_BLOCK': 87, 'END_FINALLY': 88, 'POP_EXCEPT': 89, 'STORE_NAME': 90, 'DELETE_NAME': 91, 'UNPACK_SEQUENCE': 92, 'FOR_ITER': 93, 'UNPACK_EX': 94, 'STORE_ATTR': 95, 'DELETE_ATTR': 96, 'STORE_GLOBAL': 97, 'DELETE_GLOBAL': 98, 'LOAD_CONST': 100, 'LOAD_NAME': 101, 'BUILD_TUPLE': 102, 'BUILD_LIST': 103, 'BUILD_SET': 104, 'BUILD_MAP': 105, 'LOAD_ATTR': 106, 'COMPARE_OP': 107, 'IMPORT_NAME': 108, 'IMPORT_FROM': 109, 'JUMP_FORWARD': 110, 'JUMP_IF_FALSE_OR_POP': 111, 'JUMP_IF_TRUE_OR_POP': 112, 'JUMP_ABSOLUTE': 113, 'POP_JUMP_IF_FALSE': 114, 'POP_JUMP_IF_TRUE': 115, 'LOAD_GLOBAL': 116, 'CONTINUE_LOOP': 119, 'SETUP_LOOP': 120, 'SETUP_EXCEPT': 121, 'SETUP_FINALLY': 122, 'LOAD_FAST': 124, 'STORE_FAST': 125, 'DELETE_FAST': 126, 'RAISE_VARARGS': 130, 'CALL_FUNCTION': 131, 'MAKE_FUNCTION': 132, 'BUILD_SLICE': 133, 'LOAD_CLOSURE': 135, 'LOAD_DEREF': 136, 'STORE_DEREF': 137, 'DELETE_DEREF': 138, 'CALL_FUNCTION_KW': 141, 'CALL_FUNCTION_EX': 142, 'SETUP_WITH': 143, 'LIST_APPEND': 145, 'SET_ADD': 146, 'MAP_ADD': 147, 'LOAD_CLASSDEREF': 148, 'EXTENDED_ARG': 144, 'BUILD_LIST_UNPACK': 149, 'BUILD_MAP_UNPACK': 150, 'BUILD_MAP_UNPACK_WITH_CALL': 151, 'BUILD_TUPLE_UNPACK': 152, 'BUILD_SET_UNPACK': 153, 'SETUP_ASYNC_WITH': 154, 'FORMAT_VALUE': 155, 'BUILD_CONST_KEY_MAP': 156, 'BUILD_STRING': 157, 'BUILD_TUPLE_UNPACK_WITH_CALL': 158, 'LOAD_METHOD': 160, 'CALL_METHOD': 161}

# Recovered using dump_switch_cases.py IDA plugin
# dropbox_map = {'LOAD_CLASSDEREF': 243, 'CALL_FUNCTION': 102, 'DUP_TOP': 54, 'INPLACE_FLOOR_DIVIDE': 27, 'MAP_ADD': 204, 'BINARY_XOR': 55, 'END_FINALLY': 47, 'UNPACK_EX': 131, 'RETURN_VALUE': 26, 'WITH_CLEANUP_START': 50, 'SETUP_LOOP': 108, 'BUILD_SET': 135, 'POP_TOP': 13, 'LOAD_CONST': 136, 'SETUP_FINALLY': 120, 'INPLACE_TRUE_DIVIDE': 23, 'CALL_FUNCTION_KW': 112, 'INPLACE_AND': 34, 'SETUP_ASYNC_WITH': 196, 'SETUP_EXCEPT': 101, 'INPLACE_POWER': 24, 'INPLACE_OR': 1, 'LOAD_GLOBAL': 96, 'PRINT_EXPR': 12, 'FOR_ITER': 134, 'DELETE_NAME': 132, 'BUILD_LIST': 103, 'DELETE_DEREF': 121, 'COMPARE_OP': 107, 'BINARY_OR': 28, 'UNPACK_SEQUENCE': 115, 'STORE_FAST': 139, 'LOAD_NAME': 97, 'CALL_FUNCTION_VAR': 111, 'SET_ADD': 207, 'CONTINUE_LOOP': 141, 'BUILD_TUPLE_UNPACK': 249, 'POP_JUMP_IF_FALSE': 138, 'DELETE_GLOBAL': 126, 'GET_ITER': 5, 'BINARY_ADD': 52, 'BINARY_LSHIFT': 3, 'LOAD_CLOSURE': 137, 'DUP_TOP_TWO': 18, 'IMPORT_STAR': 11, 'IMPORT_NAME': 123, 'LOAD_BUILD_CLASS': 45, 'BINARY_SUBTRACT': 62, 'INPLACE_ADD': 89, 'INPLACE_LSHIFT': 42, 'INPLACE_MODULO': 0, 'POP_EXCEPT': 44, 'BUILD_MAP': 142, 'SETUP_WITH': 118, 'INPLACE_RSHIFT': 56, 'STORE_ATTR': 95, 'BINARY_MULTIPLY': 6, 'BEFORE_ASYNC_WITH': 38, 'NOP': 67, 'LIST_APPEND': 202, 'INPLACE_XOR': 66, 'BINARY_MATRIX_MULTIPLY': 31, 'STORE_GLOBAL': 140, 'INPLACE_SUBTRACT': 69, 'STORE_NAME': 90, 'DELETE_SUBSCR': 49, 'BINARY_AND': 71, 'GET_AITER': 14, 'BREAK_LOOP': 35, 'MAKE_FUNCTION': 91, 'BUILD_MAP_UNPACK': 167, 'INPLACE_MULTIPLY': 88, 'CALL_FUNCTION_VAR_KW': 113, 'LOAD_ATTR': 110, 'BINARY_TRUE_DIVIDE': 20, 'GET_ANEXT': 85, 'ROT_TWO': 8, 'DELETE_ATTR': 109, 'POP_BLOCK': 7, 'DELETE_FAST': 93, 'EXTENDED_ARG': 144, 'STORE_DEREF': 129, 'INPLACE_MATRIX_MULTIPLY': 16, 'UNARY_NEGATIVE': 78, 'UNARY_POSITIVE': 43, 'YIELD_FROM': 2, 'UNARY_NOT': 70, 'BUILD_TUPLE': 106, 'BINARY_POWER': 37, 'STORE_SUBSCR': 72, 'BINARY_MODULO': 36, 'IMPORT_FROM': 114, 'GET_AWAITABLE': 15, 'GET_YIELD_FROM_ITER': 41, 'POP_JUMP_IF_TRUE': 119, 'JUMP_IF_FALSE_OR_POP': 98, 'BUILD_LIST_UNPACK': 206, 'LOAD_DEREF': 130, 'RAISE_VARARGS': 104, 'LOAD_FAST': 94, 'JUMP_IF_TRUE_OR_POP': 128, 'BINARY_FLOOR_DIVIDE': 83, 'BINARY_RSHIFT': 51, 'BUILD_MAP_UNPACK_WITH_CALL': 234, 'BINARY_SUBSCR': 65, 'YIELD_VALUE': 40, 'ROT_THREE': 21, 'BUILD_SET_UNPACK': 244, 'UNARY_INVERT': 32, 'BUILD_SLICE': 125, 'WITH_CLEANUP_FINISH': 48, 'JUMP_ABSOLUTE': 116, 'MAKE_CLOSURE': 124, 'JUMP_FORWARD': 92}  # old dropbox

# Recovered using dump_switch_cases.py IDA plugin
# dropbox_map = {'LOAD_CLASSDEREF': 217, 'CALL_FUNCTION': 125, 'DUP_TOP': 66, 'LOAD_METHOD': 231, 'INPLACE_FLOOR_DIVIDE': 65, 'MAP_ADD': 176, 'BINARY_XOR': 36, 'BREAK_LOOP': 18, 'UNPACK_EX': 122, 'RETURN_VALUE': 10, 'POP_BLOCK': 48, 'BUILD_SET': 107, 'POP_TOP': 24, 'LOAD_CONST': 139, 'SETUP_FINALLY': 119, 'INPLACE_TRUE_DIVIDE': 89, 'CALL_FUNCTION_KW': 135, 'INPLACE_AND': 68, 'SETUP_ASYNC_WITH': 249, 'INPLACE_POWER': 8, 'INPLACE_OR': 63, 'LOAD_GLOBAL': 130, 'LOAD_NAME': 115, 'FOR_ITER': 94, 'DELETE_NAME': 102, 'BUILD_LIST': 132, 'DELETE_DEREF': 111, 'COMPARE_OP': 92, 'BINARY_OR': 52, 'UNPACK_SEQUENCE': 116, 'STORE_FAST': 97, 'SET_ADD': 150, 'CONTINUE_LOOP': 110, 'BUILD_TUPLE_UNPACK': 187, 'POP_JUMP_IF_FALSE': 117, 'DELETE_GLOBAL': 103, 'GET_ITER': 46, 'SETUP_ANNOTATIONS': 17, 'BINARY_LSHIFT': 11, 'LOAD_CLOSURE': 120, 'DUP_TOP_TWO': 5, 'IMPORT_STAR': 22, 'IMPORT_NAME': 108, 'LOAD_BUILD_CLASS': 14, 'BINARY_SUBTRACT': 20, 'INPLACE_ADD': 6, 'INPLACE_LSHIFT': 55, 'INPLACE_MODULO': 81, 'STORE_ATTR': 140, 'BUILD_MAP': 91, 'SETUP_WITH': 105, 'DELETE_FAST': 104, 'GET_YIELD_FROM_ITER': 53, 'BUILD_CONST_KEY_MAP': 252, 'BEFORE_ASYNC_WITH': 35, 'NOP': 87, 'LIST_APPEND': 247, 'INPLACE_XOR': 47, 'BINARY_MATRIX_MULTIPLY': 9, 'STORE_GLOBAL': 128, 'INPLACE_SUBTRACT': 13, 'STORE_NAME': 90, 'DELETE_SUBSCR': 84, 'BINARY_AND': 72, 'GET_AITER': 50, 'END_FINALLY': 85, 'MAKE_FUNCTION': 142, 'BUILD_MAP_UNPACK': 146, 'INPLACE_MULTIPLY': 64, 'POP_EXCEPT': 23, 'LOAD_ATTR': 127, 'BINARY_TRUE_DIVIDE': 62, 'GET_ANEXT': 42, 'ROT_TWO': 1, 'GET_AWAITABLE': 57, 'WITH_CLEANUP_START': 3, 'INPLACE_RSHIFT': 59, 'EXTENDED_ARG': 144, 'CALL_METHOD': 174, 'STORE_DEREF': 121, 'INPLACE_MATRIX_MULTIPLY': 76, 'UNARY_NEGATIVE': 49, 'UNARY_POSITIVE': 77, 'YIELD_FROM': 45, 'UNARY_NOT': 69, 'BUILD_TUPLE': 114, 'BINARY_POWER': 74, 'STORE_SUBSCR': 56, 'BINARY_MODULO': 58, 'IMPORT_FROM': 137, 'DELETE_ATTR': 143, 'BINARY_MULTIPLY': 88, 'POP_JUMP_IF_TRUE': 123, 'JUMP_IF_FALSE_OR_POP': 101, 'FORMAT_VALUE': 180, 'LOAD_DEREF': 109, 'RAISE_VARARGS': 112, 'BUILD_SLICE': 106, 'JUMP_IF_TRUE_OR_POP': 129, 'BINARY_FLOOR_DIVIDE': 7, 'BINARY_RSHIFT': 28, 'JUMP_ABSOLUTE': 100, 'BUILD_MAP_UNPACK_WITH_CALL': 160, 'PRINT_EXPR': 44, 'BUILD_STRING': 216, 'BINARY_SUBSCR': 37, 'YIELD_VALUE': 38, 'ROT_THREE': 83, 'BUILD_SET_UNPACK': 193, 'BINARY_ADD': 2, 'UNARY_INVERT': 80, 'LOAD_FAST': 95, 'WITH_CLEANUP_FINISH': 40, 'CALL_FUNCTION_EX': 136, 'JUMP_FORWARD': 131, 'BUILD_TUPLE_UNPACK_WITH_CALL': 187, 'BUILD_LIST_UNPACK': 187, 'SETUP_LOOP': 126, 'SETUP_EXCEPT': 119}
# dropbox_map = {'LOAD_CLASSDEREF': 217, 'CALL_FUNCTION': 125, 'DUP_TOP': 66, 'LOAD_METHOD': 231, 'INPLACE_FLOOR_DIVIDE': 65, 'MAP_ADD': 176, 'BINARY_XOR': 36, 'BREAK_LOOP': 18, 'UNPACK_EX': 122, 'RETURN_VALUE': 10, 'POP_BLOCK': 48, 'BUILD_SET': 107, 'POP_TOP': 24, 'LOAD_CONST': 139, 'SETUP_FINALLY': 119, 'INPLACE_TRUE_DIVIDE': 89, 'CALL_FUNCTION_KW': 135, 'INPLACE_AND': 68, 'SETUP_ASYNC_WITH': 249, 'INPLACE_POWER': 8, 'INPLACE_OR': 63, 'LOAD_GLOBAL': 130, 'LOAD_NAME': 115, 'FOR_ITER': 94, 'DELETE_NAME': 102, 'BUILD_LIST': 132, 'DELETE_DEREF': 111, 'COMPARE_OP': 92, 'BINARY_OR': 52, 'UNPACK_SEQUENCE': 116, 'STORE_FAST': 97, 'SET_ADD': 150, 'CONTINUE_LOOP': 110, 'BUILD_TUPLE_UNPACK': 187, 'POP_JUMP_IF_FALSE': 117, 'DELETE_GLOBAL': 103, 'GET_ITER': 46, 'SETUP_ANNOTATIONS': 17, 'BINARY_LSHIFT': 11, 'LOAD_CLOSURE': 120, 'DUP_TOP_TWO': 5, 'IMPORT_STAR': 22, 'IMPORT_NAME': 108, 'LOAD_BUILD_CLASS': 14, 'BINARY_SUBTRACT': 20, 'INPLACE_ADD': 6, 'INPLACE_LSHIFT': 55, 'INPLACE_MODULO': 81, 'STORE_ATTR': 140, 'BUILD_MAP': 91, 'SETUP_WITH': 105, 'DELETE_FAST': 104, 'GET_YIELD_FROM_ITER': 53, 'BUILD_CONST_KEY_MAP': 252, 'BEFORE_ASYNC_WITH': 35, 'NOP': 87, 'LIST_APPEND': 247, 'INPLACE_XOR': 47, 'BINARY_MATRIX_MULTIPLY': 9, 'STORE_GLOBAL': 128, 'INPLACE_SUBTRACT': 13, 'STORE_NAME': 90, 'DELETE_SUBSCR': 84, 'BINARY_AND': 72, 'GET_AITER': 50, 'END_FINALLY': 85, 'MAKE_FUNCTION': 142, 'BUILD_MAP_UNPACK': 146, 'INPLACE_MULTIPLY': 64, 'POP_EXCEPT': 23, 'LOAD_ATTR': 127, 'BINARY_TRUE_DIVIDE': 62, 'GET_ANEXT': 42, 'ROT_TWO': 1, 'GET_AWAITABLE': 57, 'WITH_CLEANUP_START': 3, 'INPLACE_RSHIFT': 59, 'EXTENDED_ARG': 144, 'CALL_METHOD': 174, 'STORE_DEREF': 121, 'INPLACE_MATRIX_MULTIPLY': 76, 'UNARY_NEGATIVE': 49, 'UNARY_POSITIVE': 77, 'YIELD_FROM': 45, 'UNARY_NOT': 69, 'BUILD_TUPLE': 114, 'BINARY_POWER': 74, 'STORE_SUBSCR': 56, 'BINARY_MODULO': 58, 'IMPORT_FROM': 137, 'DELETE_ATTR': 143, 'BINARY_MULTIPLY': 88, 'POP_JUMP_IF_TRUE': 123, 'JUMP_IF_FALSE_OR_POP': 101, 'FORMAT_VALUE': 180, 'LOAD_DEREF': 109, 'RAISE_VARARGS': 112, 'BUILD_SLICE': 106, 'JUMP_IF_TRUE_OR_POP': 129, 'BINARY_FLOOR_DIVIDE': 7, 'BINARY_RSHIFT': 28, 'JUMP_ABSOLUTE': 100, 'BUILD_MAP_UNPACK_WITH_CALL': 160, 'PRINT_EXPR': 44, 'BUILD_STRING': 216, 'BINARY_SUBSCR': 37, 'YIELD_VALUE': 38, 'ROT_THREE': 83, 'BUILD_SET_UNPACK': 193, 'BINARY_ADD': 2, 'UNARY_INVERT': 80, 'LOAD_FAST': 95, 'WITH_CLEANUP_FINISH': 40, 'CALL_FUNCTION_EX': 136, 'JUMP_FORWARD': 131, 'SETUP_LOOP': 126, 'SETUP_EXCEPT': 119}

# [-] Missing mapping for {'BUILD_TUPLE_UNPACK_WITH_CALL', 'BUILD_TUPLE_UNPACK', 'BUILD_LIST_UNPACK'} -> TUPLE ~ (187, 200, 209) <This part needs to be recovered perfectly by seeing the disassembly of BUILD_TUPLE_UNPACK switch case in IDA>  and {'SETUP_LOOP', 'SETUP_EXCEPT', 'SETUP_FINALLY'} ~ (119, 126, 141) <This part doesn't need to be recovered perfectly. See Python/ceval.c to see why this is the case>
dropbox_map = {'LOAD_CLASSDEREF': 217, 'CALL_FUNCTION': 125, 'DUP_TOP': 66, 'LOAD_METHOD': 231, 'INPLACE_FLOOR_DIVIDE': 65, 'MAP_ADD': 176, 'BINARY_XOR': 36, 'BREAK_LOOP': 18, 'UNPACK_EX': 122, 'RETURN_VALUE': 10, 'POP_BLOCK': 48, 'BUILD_SET': 107, 'POP_TOP': 24, 'LOAD_CONST': 139, 'SETUP_LOOP': 119, 'INPLACE_TRUE_DIVIDE': 89, 'CALL_FUNCTION_KW': 135, 'INPLACE_AND': 68, 'SETUP_ASYNC_WITH': 249, 'INPLACE_POWER': 8, 'INPLACE_OR': 63, 'LOAD_GLOBAL': 130, 'LOAD_NAME': 115, 'FOR_ITER': 94, 'DELETE_NAME': 102, 'BUILD_LIST': 132, 'DELETE_DEREF': 111, 'COMPARE_OP': 92, 'BINARY_OR': 52, 'UNPACK_SEQUENCE': 116, 'STORE_FAST': 97, 'SET_ADD': 150, 'CONTINUE_LOOP': 110, 'BUILD_TUPLE_UNPACK_WITH_CALL': 200, 'POP_JUMP_IF_FALSE': 117, 'DELETE_GLOBAL': 103, 'GET_ITER': 46, 'SETUP_ANNOTATIONS': 17, 'BINARY_LSHIFT': 11, 'LOAD_CLOSURE': 120, 'DUP_TOP_TWO': 5, 'IMPORT_STAR': 22, 'IMPORT_NAME': 108, 'LOAD_BUILD_CLASS': 14, 'BINARY_SUBTRACT': 20, 'INPLACE_ADD': 6, 'INPLACE_LSHIFT': 55, 'INPLACE_MODULO': 81, 'STORE_ATTR': 140, 'BUILD_MAP': 91, 'SETUP_WITH': 105, 'DELETE_FAST': 104, 'GET_YIELD_FROM_ITER': 53, 'BUILD_CONST_KEY_MAP': 252, 'BEFORE_ASYNC_WITH': 35, 'NOP': 87, 'LIST_APPEND': 247, 'INPLACE_XOR': 47, 'BINARY_MATRIX_MULTIPLY': 9, 'STORE_GLOBAL': 128, 'INPLACE_SUBTRACT': 13, 'STORE_NAME': 90, 'DELETE_SUBSCR': 84, 'BINARY_AND': 72, 'GET_AITER': 50, 'END_FINALLY': 85, 'MAKE_FUNCTION': 142, 'BUILD_MAP_UNPACK': 146, 'INPLACE_MULTIPLY': 64, 'POP_EXCEPT': 23, 'LOAD_ATTR': 127, 'BINARY_TRUE_DIVIDE': 62, 'GET_ANEXT': 42, 'ROT_TWO': 1, 'GET_AWAITABLE': 57, 'WITH_CLEANUP_START': 3, 'INPLACE_RSHIFT': 59, 'EXTENDED_ARG': 144, 'CALL_METHOD': 174, 'STORE_DEREF': 121, 'INPLACE_MATRIX_MULTIPLY': 76, 'UNARY_NEGATIVE': 49, 'UNARY_POSITIVE': 77, 'YIELD_FROM': 45, 'UNARY_NOT': 69, 'BUILD_TUPLE': 114, 'BINARY_POWER': 74, 'STORE_SUBSCR': 56, 'BINARY_MODULO': 58, 'IMPORT_FROM': 137, 'DELETE_ATTR': 143, 'BINARY_MULTIPLY': 88, 'POP_JUMP_IF_TRUE': 123, 'JUMP_IF_FALSE_OR_POP': 101, 'FORMAT_VALUE': 180, 'LOAD_DEREF': 109, 'RAISE_VARARGS': 112, 'BUILD_SLICE': 106, 'JUMP_IF_TRUE_OR_POP': 129, 'BINARY_FLOOR_DIVIDE': 7, 'BINARY_RSHIFT': 28, 'JUMP_ABSOLUTE': 100, 'BUILD_MAP_UNPACK_WITH_CALL': 160, 'PRINT_EXPR': 44, 'BUILD_STRING': 216, 'BINARY_SUBSCR': 37, 'YIELD_VALUE': 38, 'ROT_THREE': 83, 'BUILD_SET_UNPACK': 193, 'BINARY_ADD': 2, 'UNARY_INVERT': 80, 'LOAD_FAST': 95, 'WITH_CLEANUP_FINISH': 40, 'CALL_FUNCTION_EX': 136, 'JUMP_FORWARD': 131, 'SETUP_EXCEPT': 126, 'SETUP_FINALLY': 141, 'BUILD_TUPLE_UNPACK': 200, 'BUILD_LIST_UNPACK': 209, 'SETUP_EXCEPT': 126, 'SETUP_FINALLY': 141}

print("// [+] %s%% of the opcodes were recovered automatically using static analysis!\n" % str((len(dropbox_map.keys()) - 3) / len(dropbox_map.keys()) * 100))

opcode_map = {}

for k, v in dropbox_map.items():
    nv = original_map[k]

    opcode_map[v] = nv

diff = set(original_map.keys()) - set(dropbox_map.keys())

if diff:
    print("// [-] Missing mapping for", diff)
    pass

# print(opcode_map)


# Generate C opcode map
out = [255] * 255
for k, v in opcode_map.items():
    out[k] = v
x = "%s" % out
x = x.replace("[", "").replace("]", "")
print("unsigned char opcode_map[255] = { %s };" % x)


# print(out)

"""
<OLD>

print(out[136])  # should be 100

reverse_out = [255] * 255
for k, v in opcode_map.items():
    reverse_out[v] = k

hasjrel = [93, 110, 120, 121, 122, 143, 154]
out = [reverse_out[i] for i in hasjrel]
print(out)

hasjabs = [111, 112, 113, 114, 115, 119]
out = [reverse_out[i] for i in hasjabs]
print(out)

hasname = [90, 91, 95, 96, 97, 98, 101, 106, 108, 109, 116, 127]
out = [reverse_out[i] for i in hasname]
print(out)

haslocal = [124, 125, 126]
out = [reverse_out[i] for i in haslocal]
print(out)

hasfree = [135, 136, 137, 138, 148]
out = [reverse_out[i] for i in hasfree]
print(out)
"""
