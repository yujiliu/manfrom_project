import TableLite from "vue3-table-lite";

const table = reactive({
  isLoading: false,
  isReSearch: false,
  columns: [
    {
      label: "ID",
      field: "id",
      width: "3%",
      sortable: true,
      isKey: true,
    },
    {
      label: "Name",
      field: "name",
      width: "10%",
      sortable: true,
      display: function (row) {
        return (
          '<a href="#" data-id="' + row.user_id + '" class="name-btn">' + row.name + "</button>"
        );
      },
    },
    {
      label: "Email",
      field: "email",
      width: "15%",
      sortable: true,
    },
    {
      label: "",
      field: "quick",
      width: "10%",
      display: function (row) {
        return (
          '<button type="button" data-id="' + row.user_id + '" class="quick-btn">Button</button>'
        );
      },
    },
  ],
  rows: [
      {
        id: 1,
        name: "TEST1"
      },
      {
        id: 2,
        name: "TEST2"
      }
  ],
  totalRecordCount: 2,
  sortable: {
    order: "id",
    sort: "asc",
  },
  messages: {
    pagingInfo: "Showing {0}-{1} of {2}",
    pageSizeChangeLabel: "Row count:",
    gotoPageLabel: "Go to page:",
    noDataAvailable: "No data",
  },
});
