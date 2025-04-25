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
  box-shadow: 0 1px 2px gray;
}

th,
td {
  text-align: left;
  padding: 5px 10px;
  border-bottom: 1px solid gray;
  word-break: break-all;
}

th {
  background-color: lightgray;
}

tr:hover {
  background-color: whitesmoke;
}
</style>
