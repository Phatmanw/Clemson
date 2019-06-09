#include "hybrid.h"

char *bitmap_allocate() {
  char *p = arena_head[0];
  arena_head[0] += ARENA_0_BLOCK_SIZE;
  arena_count[0]--;

  return p + 8;
}


char *list_allocate (int size) {
  char *p = arena_head[size];
  int block_size = 0;
  if (size == 1) { block_size = ARENA_1_BLOCK_SIZE; }
  else { block_size = ARENA_2_BLOCK_SIZE; }
  arena_head[size] += block_size;
  arena_count[size]--;

  return p;
}

char *allocate (int size) {
  if (size <= 0) {
    return NULL;
  }
  else if (size <= (arena_block_size[0] - 8)) {

    return bitmap_allocate();
  }
  else if (size <= (arena_block_size[1] - 8)) {

    return list_allocate (1);
  }
  else if (size <= (arena_block_size[2] - 8 )) {

    return list_allocate (2);
  }
  else {
    return NULL;
  }
}

void release (char *release_ptr) {

}
