import React, { useMemo, useState } from "react";
import {
	  useReactTable,
	  getCoreRowModel,
	  getSortedRowModel,
	  flexRender,
} from "@tanstack/react-table";

const tableHeaders = [
	  "Name", "Elo", "Total Stars", "Destruction %",
	  "3 Stars", "2 Stars", "1 Stars", "0 Stars",
	  "Missed Attacks", "Total Attacks"
];

const EloTable = ({ clanmemberelo }) => {
  const data = useMemo(() => {
    return clanmemberelo.map((row) => {
      const obj = {};
      tableHeaders.forEach((header, i) => {
        obj[header] = row[i];
      });
      return obj;
    });
  }, [clanmemberelo]);

  const columns = useMemo(() => {
    return tableHeaders.map((header) => ({
      accessorKey: header,
      header: () => <span>{header}</span>,
      cell: (info) => info.getValue(),
    }));
  }, []);

  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
  });

  return (
    <div className="elo-table-container">
      <table className="elo-table">
        <thead>
          {table.getHeaderGroups().map((headerGroup) => (
            <tr key={headerGroup.id}>
              {headerGroup.headers.map((header) => (
                <th
                  key={header.id}
                  onClick={header.column.getToggleSortingHandler()}
                  style={{ cursor: "pointer" }}
                >
		  {flexRender(header.column.columnDef.header, header.getContext())}
	          {{
	            asc: " 🔼",
	            desc: " 🔽"
	          }[header.column.getIsSorted()] ?? null}
	        </th>
	      ))}
	  </tr>
        ))}
      </thead>
    <tbody>
      {table.getRowModel().rows.map((row) => (
        <tr key={row.id}>
          {row.getVisibleCells().map((cell) => (
             <td key={cell.id}>
               {flexRender(cell.column.columnDef.cell, cell.getContext())}
             </td>
           ))}
         </tr>
       ))}
     </tbody>
   </table>
 </div>
 );
};

export default EloTable;
