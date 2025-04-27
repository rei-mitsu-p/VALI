<template>
  <table>
    <thead>
      <tr>
        <th v-for="col in columns" :key="col.key">
          {{ col.label }}
        </th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(row, i) in rows" :key="i">
        <td v-for="col in columns" :key="col.key">
          <template v-if="$slots[col.key]">
            <slot :name="col.key" :row="row"></slot>
          </template>
          <template v-else>
            {{ row[col.key] }}
          </template>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup lang="ts">
defineProps<{
  columns: Array<{ key: string; label: string }>;
  rows: Array<Record<string, string>>;
}>();
</script>

<style scoped>
table {
  border-collapse: collapse;
  box-shadow: 0 0 1px gray;
  word-break: break-all;
}

th,
td {
  text-align: left;
  padding: 5px;
  border-bottom: 1px solid gray;
}

th {
  background-color: lightgray;
}

tbody tr:hover {
  background-color: whitesmoke;
}
</style>
