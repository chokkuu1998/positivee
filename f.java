public static Optional<String> findMiddleElementLinkedList(
  LinkedList<String> linkedList)
  {
    if (linkedList == null || linkedList.isEmpty())
    {
        return Optional.empty();
    }
 
    return Optional.of(linkedList.get(
      (linkedList.size() - 1) / 2));
}
